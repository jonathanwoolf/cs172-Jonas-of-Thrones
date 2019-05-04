#TODO:
#1. Get follwer ids (enqueueFollowers function)
#2. pop_front function
#3. implement queue functionality
#4. Enforce num-hops

import tweepy
import sys
import json
import os
import lxml.html

#get keys
f = open("twitterkeys.txt", "r")
f1 = f.readlines()
access_key = str(f1[0])
access_secret = str(f1[1])
consumer_key = str(f1[2])
consumer_secret = str(f1[3])
access_key = access_key[:-1]
access_secret = access_secret[:-1]
consumer_key = consumer_key[:-1]
consumer_secret = consumer_secret[:-1]

def download_tweets(user_handle, tweet_count, num_hops, output_dir):
    #authorize customer/access keys and secrets
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    #use twitter API to retrieve tweets
    api = tweepy.API(auth)
    file_cnt = 1
    curr_filename = 'tweets_' + str(file_cnt) + '.txt'
    i = 1
    tweetList = [dict() for x in range(0)]
        
    while(tweet_count > 0):
        if(tweet_count == 0):
            break
        #while(len(follower_queue) > 0):
        batch_count = min(tweet_count, 100)
        #user_handle = pop_front(follower_queue)
        tweets = api.user_timeline(id=user_handle,count=batch_count,tweet_mode='extended')
        #enqueueFollowers(user_handle)
        for tweet in tweets:
            print(tweet.entities['urls'])
#             if (len(tweet.entities['urls']) != 0):
#                 tempURL = str(tweet.entities['urls'][0]['expanded_url'])
#             else:
#                 tempURL = ""
#             if (tempURL != ""):
#                 t = lxml.html.parse(tempURL)
#                 URLtitle = str(t.find(".//title").text)
#             else:
#                 URLtitle = ""
            data = {
                "Author": tweet.author.name,
                "Text": tweet.full_text,
                "Date": str(tweet.created_at),
                #"Link": tempURL,
                #"Link Title": URLtitle,
                "Geo": tweet.geo
            }
            tweetList.append(data)
            ++i
            if(i >= 5000):
                with open(curr_filename, 'w+') as outfile:
                    for entry in tweetList:
                        json.dump(entry, outfile)
                        outfile.write('\n')
                ++file_cnt
                curr_filename = 'tweets_' + str(file_cnt) + '.json'
                i = 0
                tweetList = [dict() for x in range(0)]
                    
        tweet_count = tweet_count - len(tweets)
        if(tweet_count == 0):
            with open(curr_filename, 'w+') as outfile:
                for entry in tweetList:
                    json.dump(entry, outfile)
                    outfile.write('\n')
            
def main():
    #parse argv (command line arguments) for starting user_handle, tweet_count and num_hops
    inputs = sys.argv[1:]
    if(len(inputs) >= 1):
        user_handle = str(inputs[0])
    else:
        user_handle = "nytimes"
    if(len(inputs) >= 2):
        tweet_count = int(inputs[1])
    else:
        tweet_count = 5
    if(len(inputs) >= 3):
        num_hops = int(inputs[2])
    else:
        num_hops = 1
    if(len(inputs) >= 4):
        output_dir = int(inputs[3])
    else:
        output_dir = "default"
    #call download_tweets with necessary info
    download_tweets(user_handle, tweet_count, num_hops, output_dir)

main()