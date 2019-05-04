import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys
import json
from urllib.request import urlopen
import lxml.html
import os

#get keys
fp = open("twitterkeys.txt", "r")
f1 = fp.readlines()
access_key = str(f1[0])
access_secret = str(f1[1])
consumer_key = str(f1[2])
consumer_secret = str(f1[3])
access_key = access_key[:-1]
access_secret = access_secret[:-1]
consumer_key = consumer_key[:-1]
consumer_secret = consumer_secret[:-1]

#parse command line arguments(seeding keyword, # of tweets, directory)
if (len(sys.argv) > 1):
    keyword = str(sys.argv[1])
else:
    keyword = "Trump"
if (len(sys.argv) > 2):
    tweet_count = int(sys.argv[2])
else:
    tweet_count = 10
if (len(sys.argv) > 3):
    dirName = str(sys.argv[3])
else:
    dirName = "data"
fileCount = 1
filename = dirName + '/' + 'tweets_' + str(fileCount) + '.json'
f = open(filename, 'w+')

#twitter listener for streaming
class twitterListener(StreamListener):

    def __init__(self, api=None):
        super(twitterListener, self).__init__()

    def on_data(self, data):
        global keyword
        global tweet_count
        global fileCount
        global filename
        global f
        if(tweet_count <= 0):
            f.close()
            return False
        tweet = json.loads(data)
        if (len(tweet['entities']['urls']) != 0):
            tempURL = str(tweet['entities']['urls'][0]['expanded_url'])
        else:
            tempURL = ""
        if (tempURL != ""):
            html = urlopen(tempURL)
            t = lxml.html.parse(html)
            URLtitle = str(t.find(".//title").text)
        else:
            URLtitle = ""
        #so tweets dont get truncated
        if 'extended_tweet' in tweet:
            if 'full_text' in tweet['extended_tweet']:
                text = tweet['extended_tweet']['full_text']
            else:
                text = tweet['text']
        elif 'text' in tweet:
            text = tweet['text']
        data = {
            "Author": tweet['user']['name'],
            "Text": text,
            "Date": tweet['created_at'],
            "Link": tempURL,
            "Link Title": URLtitle,
            "Geo": tweet['coordinates']
        }
        tweet_count = tweet_count - 1
        dataString = str(json.dumps(data))
        f.write(dataString)
        f.write('\n')
        statinfo = os.stat(filename)
        if(statinfo.st_size > (10 * 1024 * 1024)):
            f.close()
            ++fileCount
            filename = dirName + '/' + 'tweets_' + str(fileCount) + '.json'
            f = open(filename, 'w+')
        return True

    def on_error(self, status):
        print(status)
        return False

#call stream listener
l = twitterListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
stream = Stream(auth, l)
stream.filter(track=[keyword],languages=["en"]) 