import tweepy # type: ignore
from dotenv import load_dotenv # type: ignore
from random import shuffle
import os
import time
import random

# load keys
load_dotenv()

# get APIs to read via getenv() 
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# access APIs via tweepy.Client
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# test authentication
try:
    user = client.get_me().data
    print(f'Authenticated as {user.name}')
except:
    print('Authentication Error!')

# access the quotes file and clean the white spaces and checks its and then appends to quotes.
with open('quotes.txt','r',encoding='utf-8') as file:
    quotes = []
    for line in file:
        cleaned_line = line.strip()
        if cleaned_line:
            if len(cleaned_line) > 280:
                print('Quotes charactor exceeded 280! ')
            else:
                quotes.append(cleaned_line)

# Intial length of quotes
initial_quote = len(quotes)    # Python assigns the integer value of len(quotes) and This is a copy of the number,not a link to the list.

# shuffle the quotes
def shuffle_list():
    shuffle(quotes)
    return quotes

# the logic
daily_quotes = 0
popped_quotes=[]
quotes_tracking = 0

while len(popped_quotes) < initial_quote:
    if not quotes:
        print('All the quotes are posted!')
        break

    shuffle_list()
    remove = quotes.pop()
    combined_text = f'{remove}\nTweeted by my bot!'
    quotes_tracking += 1
    print(f'Total number of posts used: {quotes_tracking}')

    try:
        if len(combined_text) <= 280:
            response = client.create_tweet(text=combined_text)
            print(f'Tweeted Quote: {remove} at {time.ctime()}')
            popped_quotes.append(remove)
                     
        else:
            print('Combined text exceeded 280!')
            print(f'Extra texts: {combined_text[280:]}')

    except Exception as e:
        print(f'Error: {e}')
        
        if "429" in str(e):
            print("Rate limit hit. Waiting 15 minutes...")
            time.sleep(900)
        break
    
    
    if len(popped_quotes) % 2 == 0 and len(popped_quotes)> 0:  # After first of pair
        time.sleep(12 * 3600)  # 12-hour gap

print('All the quotes processed!')
    

