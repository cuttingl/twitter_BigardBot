import tweepy
import datetime
import os


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
    auth = tweepy.OAuthHandler(tokens[0], tokens[1])
    auth.set_access_token(tokens[2], tokens[3])
    api = tweepy.API(auth)

    
    publishTweetFromInput(api)




