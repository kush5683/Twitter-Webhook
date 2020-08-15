import tweepy 
import json
import random
from dhooks import Webhook

hook = Webhook('https://discord.com/api/webhooks/743532090024525895/Q_gCOl0ae0zoubQRukQUp-7dNZk_w38FTN4GLfnhLZpHTRedVA4SVNAoTD0U2u9m1CCM')
print('Booted up')
hook.send('!clear')
hook.send('I am here')

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
    tweets = api.user_timeline(screen_name='Rainbow6Game', count=100, include_rts=True)
    for tweet in tweets:
        if tweet.in_reply_to_status_id is None:
            return tweet
        
try:
    hook.send(get_tweet().full_text)
except:
    hook.send(get_tweet().text)
    
    
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        #status._json['user']['id'] == author and 
        if status.in_reply_to_status_id is None:
            message = status.text
            try:
                message = status.full_text
            except:
                message = status.text
            print(message)
            hook.send(message)
            
            
            
        
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener,tweet_mode='extended')
myStream.filter(follow=["399404516"],is_async=True)

#399404516
#740583606775582723



    

