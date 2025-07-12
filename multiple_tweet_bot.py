import tweepy # type: ignore
from dotenv import load_dotenv # type: ignore
import os
import time
import random

# Load environment variables
load_dotenv()

# Twitter API credentials
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Debug: Check credentials
print("CONSUMER_KEY:", consumer_key)
print("CONSUMER_SECRET:", consumer_secret)
print("ACCESS_TOKEN:", access_token)
print("ACCESS_TOKEN_SECRET:", access_token_secret)

if None in (consumer_key, consumer_secret, access_token, access_token_secret):
    raise ValueError("One or more credentials are missing. Check .env file.")

# Initialize tweepy Client (API v2)
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Test authentication
try:
    user = client.get_me().data
    print("Authenticated as:", user.name)
except Exception as e:
    print(f"Authentication error: {e}")

# List of base tweet messages and hashtags
hashtags = ["#Bitcoin", "#Crypto", "#Blockchain", "#Web3"]

tweets = [
    "Exploring {hashtag} trends! 🚀",
    "Loving the {hashtag} community!",
    "Learning more about {hashtag} with Python!"
]

# Post tweets periodically
post = 0
max_post = 10
while post < max_post:
    # Create a unique tweet
    tweet_text = f"{random.choice(tweets).format(hashtag=random.choice(hashtags))} Posted at {time.ctime()}" # .format hastag refers to the hastag inside tweets.
    try:
        response = client.create_tweet(text=tweet_text)
        print(f"Posted tweet: {tweet_text} (ID: {response.data['id']})")
        post +=1
    except Exception as e:
        print(f"Error posting tweet: {e}")
    time.sleep(3600)  # Wait 1 hour (3600 seconds)

print(f'Post reached its daily limits of {post}')