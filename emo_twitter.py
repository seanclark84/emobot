from twython import Twython, TwythonError
from random import sample, choice
from time import sleep
import datetime
import sys
import configparser

file = sys.argv[1]
config = configparser.ConfigParser()
config.read(file)

APP_KEY = config.get('authentication', 'app_key') 
APP_SECRET = config.get('authentication', 'app_secret')
OAUTH_TOKEN = config.get('authentication', 'token')
OAUTH_TOKEN_SECRET = config.get('authentication', 'token_secret')
MAX_RESULTS = 10

emotion = {'date':None, 'message':None}

def get_emotion(twitter):
    currentdate = datetime.datetime.now().date()
    if currentdate != emotion['date']:
        emotion['date'] = currentdate
        emotion['message'] = "I am " + generate_emotion()
        twitter.update_status(status="Today " + emotion['message'] + "...")
    return emotion['message']
    
def generate_emotion():
    with open('emotions.txt') as f:
        content = f.readlines()
    content = list(map(lambda s: s.strip(), content))
    print(content)
    return choice(content)

# Main functionality
while True:
    # create twitter interface
    twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    
    # generate an emotion per day
    emo = get_emotion(twitter)
    print("Emotion is " + emo)
    
    # get the results
    result = twitter.search(q=emo,lang='en')
    tweets = result['statuses']
    
    # take a sample of the results
    sample_tweets = tweets if len(tweets) < MAX_RESULTS else sample(tweets, MAX_RESULTS)
    
    # attempt to tweet
    for tweet in sample_tweets:
        try:
            print("Retweeting something: " + tweet['id_str'])
            twitter.retweet(id = tweet['id'])
        except TwythonError: 
            print('Error caught - ignoring')
    #sleep(60*15)
    sleep(60*10)
    

