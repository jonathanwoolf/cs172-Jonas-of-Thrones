#TODO:
#1. Get friends/count num_hops

import tweepy
import sys
import json
import os

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
    curr_filename = 'tweets_' + str(file_cnt) + '.json'
        
    while(tweet_count > 0):
        #while(len(follower_queue) > 0):
        if(tweet_count >= 100):
            #user_handle = pop_front(follower_queue)
            tweets = api.user_timeline(id=user_handle,count=100,tweet_mode='extended')
            #enqueueFollowers(user_handle)
            for tweet in tweets:
                curr_filename = 'tweets_' + str(file_cnt) + '.json'
                data = {
                    "Author": tweet.author.name,
                    "Text": tweet.full_text,
                    "Geo": tweet.geo
                }
                with open(curr_filename, 'w+') as outfile:
                    json.dump(data, outfile)
                statinfo = os.stat(curr_filename)
                if(statinfo.st_size > (10 * 1024 *1024)):
                    ++file_cnt
                    curr_filename = 'tweets_' + str(file_cnt) + '.json'
            tweet_count = tweet_count - len(tweets)

        else:
            #user_handle = pop_front(follower_queue)
            tweets = api.user_timeline(id=user_handle,count=tweet_count,tweet_mode='extended')
            #enqueueFollowers(user_handle)
            for tweet in tweets:
                curr_filename = 'tweets_' + str(file_cnt) + '.json'
                data = {
                    "Author": tweet.author.name,
                    "Text": tweet.full_text,
                    "Geo": tweet.geo
                }
                with open(curr_filename, 'w+') as outfile:
                    json.dump(data, outfile)
                statinfo = os.stat(curr_filename)
                if(statinfo.st_size > (10 * 1024 *1024)):
                    ++file_cnt
                    curr_filename = 'tweets_' + str(file_cnt) + '.json'
            tweet_count = tweet_count - len(tweets)
            
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