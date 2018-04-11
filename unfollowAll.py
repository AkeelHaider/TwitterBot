from time import sleep
import tweepy



consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True

api = tweepy.API(auth)

myBot = api.me()
li=api.friends_ids(myBot)

for i in li:
    print(i)
    api.destroy_friendship(i)
    print("Friendship destroyed with: ",i)



