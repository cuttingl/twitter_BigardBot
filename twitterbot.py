import tweepy
import datetime
import os
import credentials

def publishTweetFromInput(api):
    text = input("le text de votre tweet : ")
    api.update_status(text)
    print(text)

def senddmtest(api):
    api.send_direct_message('LaurentCutting', "test")
    api.send_direct_message('hugobollon', "t une énaurme merde")

if __name__ == "__main__":
    auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_KEY, credentials.ACCESS_SECRET)
    api = tweepy.API(auth)

    senddmtest(api)
    
    ##publishTweetFromInput(api)




