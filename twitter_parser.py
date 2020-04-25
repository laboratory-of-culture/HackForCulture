from twitter_scraper import get_tweets
from twitter_scraper import Profile
import time

def scrap_bio(username):
    profile = Profile(username)
    return profile.to_dict()['biography']

def scrap_tweets_text(username):
    tweets = ' '
    for tweet in get_tweets(username, pages=1):
        # TODO add translator
        tweets = tweets + tweet['text'] + ' '
    return tweets



