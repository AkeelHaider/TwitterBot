from time import sleep
import tweepy



consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
#Connection
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True

api = tweepy.API(auth)

myBot = api.me()


tweet = 'This is a Twitter Bot'
api.update_status(status=tweet)
