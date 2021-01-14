import tweepy
from datetime import datetime
import os
import credentials

def publishTweetFromInput(api):
    text = input("le text de votre tweet : ")
    api.update_status(text)
    print(text)

def senddmtest(api):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    api.send_direct_message('906078704', "test is doing fine")
    api.send_direct_message('945425370123251713', "salut hehe ceci est un test, envoyé à ... " + current_time)

if __name__ == "__main__":
    auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_KEY, credentials.ACCESS_SECRET)
    api = tweepy.API(auth)

    senddmtest(api)
    
    ##publishTweetFromInput(api)




