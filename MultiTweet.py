import tweepy, time, sys



consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True

api = tweepy.API(auth)


myBot = api.me()


filename = open("tweets.txt", 'r')
f = filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(5)  # Tweet every 15 minutes
