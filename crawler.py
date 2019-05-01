#TODO:
#1. Get friends/count num_hops

import tweepy
import sys
import json

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

def download_tweets(user_handle, tweet_count, num_hops, output_dir):
    #authorize customer/access keys and secrets
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    #use twitter API to retrieve tweets
    api = tweepy.API(auth)
    tweets = api.user_timeline(id=user_handle,count=1,tweet_mode="extended")
    #array to store tweet text
    tweetText = []
    with open ("data.json") as outfile:
        for tweet in tweets:
            print(tweet.full_text)
            data = json.dump(tweet, outfile)
        

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