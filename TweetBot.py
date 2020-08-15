import tweepy 
import json
import random
from dhooks import Webhook

hook = Webhook('https://discord.com/api/webhooks/743532090024525895/Q_gCOl0ae0zoubQRukQUp-7dNZk_w38FTN4GLfnhLZpHTRedVA4SVNAoTD0U2u9m1CCM')

version = "Build 1.0"



with open('twitter-creds.json') as f:
    data = json.load(f)
    
ACCESS_TOKEN = data['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = data['ACCESS_TOKEN_SECRET']
CONSUMER_KEY = data['CONSUMER_KEY']
CONSUMER_SECRET = data['CONSUMER_SECRET']
BEARER_TOKEN = data['BEARER_TOKEN']
callback_uri = 'oob'



            
# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET,callback_uri)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

me = api.me()

r6 = api.get_user('Rainbow6Game')
author = api.user_timeline(screen_name=r6.screen_name, count=100)[0]._json['user']['id']

def get_tweet():
    tweets = api.user_timeline(screen_name='Rainbow6Game', count=100)
    for tweet in tweets:
        if tweet.in_reply_to_status_id is None:
            return tweet

last = get_tweet()
try:
    message = last.full_text
except:
    message = last.text
hook.send(message)
hook.send(f"https://twitter.com/{last.user.screen_name}/status/{last.id}")
    
class MyStreamListener(tweepy.StreamListener):
    def on_data(self, raw_data):
        self.process_data(raw_data)
        return True

    def process_data(self, raw_data):
        return

    def on_status(self, status):
        if status._json['user']['id'] == author and status.in_reply_to_status_id is None:
            message = status.text
            try:
                message = status.full_text
            except:
                message = status.text
            print(message)
            hook.send(message)
            hook.send(f"https://twitter.com/{status.user.screen_name}/status/{status.id}")

    def on_error(self, status_code):
        if status_code == 420:
            return False
            
            
        
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener,tweet_mode='extended')
myStream.filter(follow=["399404516"],is_async=True)

#399404516
#740583606775582723



    

