import tweepy
from datetime import datetime
import os
import query_quote
#import credentials

def publishTweetFromInput(api):
    text = input("le text de votre tweet : ")
    api.update_status(text)
    print(text)
    print(text + " salut ceci est un test")

def senddmtest(api):
    api.send_direct_message('906078704', query_quote.query_quote())

def botRoutine(api):

    now = datetime.now().time()
    current_time = now.strftime("%H:%M:%S")
    while (True):
        if current_time == "19:00":
            api.update_status("""random_text_generated""")


if __name__ == "__main__":
    """auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_KEY, credentials.ACCESS_SECRET)
    api = tweepy.API(auth)"""

    ##senddmtest(api)
    now = datetime.now().time()
    current_time = now.strftime("%H:%M")
    print(current_time == "18:00")
    ##publishTweetFromInput(api)




