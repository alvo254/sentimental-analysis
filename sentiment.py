#!/usr/bin/python3
import tweepy
from textblob import TextBlob

# create a twitter app from twitter.developers and fill in the lines bellow 7 to 10 
# If unable please look for indepth tutorials on how to create a twitter app 

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
