import tweepy  # type: ignore
from dotenv import load_dotenv # type: ignore
import os
import time

# load environement 
load_dotenv() 

# read env with os.getenv
consumer_key = os.getenv("CONSUMER_KEY") 
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Access API
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

########## this is where you code about what you wanna do ############

# test authentication
user = client.get_me().data
print(f"Authenticated as: {user.name}")

# create hashtags to direct the bot to like
hastags = ['#Bitcoin','#Python']

# tell the bot to like
btc_tweet_id = '1943359374497591739'

try:
    client.create_like(tweet_id=btc_tweet_id)
    print(f'liked the post by {btc_tweet_id}')

except:
    print(f'Error')


# strip() is a string method in Python that removes leading (start) and trailing (end) whitespace characters from a line. Whitespace includes spaces, tabs, and newline characters (\n).
    

