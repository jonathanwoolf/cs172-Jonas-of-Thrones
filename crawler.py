#TODO:
#1. Get friends/count num_hops

import tweepy
import sys

#get keys
f = open("twitterkeys.txt", "r")
f1 = f.readlines()
access_key = f1[0]
access_secret = f1[1]
consumer_key = f1[2]
consumer_secret = f1[3]

def download_tweets(user_handle, tweet_count, num_hops):
    #authorize customer/access keys and secrets
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    #use twitter API to retrieve tweets
    api = tweepy.API(auth)
    tweets = api.user_timeline(screen_name=user_handle)
    #array to store tweet text
    tweetText = []
    csv_tweets = [tweet.text for tweet in tweets] #Creating CSV file for tweets
    for j in csv_tweets:
        tweetText.append(j)
    print(tweetText)

def main():
    #parse argv (command line arguments) for starting user_handle, tweet_count and num_hops
    inputs = sys.argv[1:]
    if(len(inputs) >= 1):
        user_handle = str(inputs[0])
    else:
        user_handle = ""
    if(len(inputs) >= 2):
        tweet_count = int(inputs[1])
    else:
        tweet_count = 5
    if(len(inputs) >= 3):
        num_hops = int(inputs[2])
    else:
        num_hops = 1
    #call download_tweets with necessary info
    download_tweets(user_handle, tweet_count, num_hops)

main()