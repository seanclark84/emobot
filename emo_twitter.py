from twython import Twython, TwythonError
from random import sample
from time import sleep

APP_KEY = 'T5fCyMA9KCvgqwOl1OjxB3AIJ'
APP_SECRET = 'yvdRRs4Di12vsHtoztdGcMibN7flr7MBjjJ006nxvhjQgnXNR5'
OAUTH_TOKEN = '4115035882-Z42eM4M8e1GvxG8wd8OptgKLf5pg4IbyDVrW64I'
OAUTH_TOKEN_SECRET = '4UffQdefudVAWhqkfXO0RUBck71ot8crn7ipbJJFX6qrE'

while True:
    twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    result = twitter.search(q='i am happy',lang='en')
    tweets = result['statuses']
    sample_tweets = sample(tweets, 5)
    print(sample_tweets)
    for tweet in sample_tweets:
        try:
            twitter.retweet(id = tweet['id'])
        except TwythonError: 
            print('Error caught - ignoring')
    sleep(60*15)