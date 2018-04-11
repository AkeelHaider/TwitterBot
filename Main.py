from DataManager import BotSql
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

botsql = BotSql()



print("Connected as: @" + myBot.screen_name + "\n Current database stats: \n" + botsql.get_stats())


for tweet in tweepy.Cursor(api.search, q="#VadaChennai").items(10):
    errcount = 0
    tweetid = 0
    try:

        if (tweet.user.id == myBot.id) or (botsql.check_Ban(str(tweet.user.id))) or (botsql.check_Tweet(str(tweet.id))):
            continue
        tweetid = str(tweet.id)
        botsql.add_Tweet(tweetid, str(tweet.user.id))
        print("\nUsername: @" + tweet.user.screen_name)
        if (tweet.retweeted == False):
            tweet.retweet()
            print("Retweeted the tweet: \n(( " + tweet.text + " ))")
        if tweet.user.following== False:
            tweet.user.follow()
            print("Followed user: ")

        errcount = 0
    except tweepy.TweepError as e:
        print(e)
        botsql.remove_Tweet(tweetid)
        ++errcount
        if(errcount > 10):
            print("Pausing for 30 minutes")
            time.sleep(1800)
        else:
            errcount = 0
            time.sleep(10)
        continue

print("Finished run. New database stats:\n " + botsql.get_stats())
