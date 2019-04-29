import tweepy 

consumer_key = "uWrfMtTSMKKgXIcb94vtKsoY4"
consumer_secret = "DoIbrsuvOfb2mTOynvCVT3714axq3oU9B3Rn56H1Iv87gAJQS4"
access_token = "713245552574500864-KGGynfQHNVeNStALqAu36gR1sTg65hm"
access_secret = "JMWzrC2ggLnm4ZtWd8mUHBksn4D9UzHi7N1WJZSNnGLbi"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

