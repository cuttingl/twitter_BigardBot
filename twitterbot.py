import tweepy
import datetime
import os
import credentials


def readTokens(tokens):
    with open("./tokens_bigardbot.txt", 'r') as file:
        for line in file:
            for word in line.split():
                tokens.append(word)

def publishTweetFromInput(api):
    text = input("le text de votre tweet : ")
    api.update_status(text)
    print(text)

if __name__ == "__main__":
    tokens = []
    readTokens(tokens)
    print(tokens)
    auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_KEY, credentials.ACCESS_SECRET)
    api = tweepy.API(auth)

    
    publishTweetFromInput(api)




