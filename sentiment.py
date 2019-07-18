#!/usr/bin/python3
import tweepy
from textblob import TextBlob

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

public = api.search('Obama')

for tweets in public:
    print(tweets.text)
    analysis = TextBlob(tweets.text)
    print(analysis.sentiment)