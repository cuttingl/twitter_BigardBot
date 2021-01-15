import tweepy
from datetime import datetime
import os
import query_quote
import credentials
import pymysql
import random

def publishTweetFromInput(api):
    text = input("le text de votre tweet : ")
    api.update_status(text)
    print(text)
    print(text + " salut ceci est un test")

def senddmtest(api, connection):
    with connection:
        with connection.cursor() as cursor:
            # Create a new record
            sql1 = "SELECT COUNT(*) FROM bigardTwitterBot"
            query1 = cursor.execute(sql1)
            result1 = cursor.fetchone()
            numrandom = random.randint(0, int(result1[0])-1)
            print(numrandom)
            sql = "SELECT `citation` FROM bigardTwitterBot WHERE `id`="+ str(numrandom)
            cursor.execute(sql)
            result = cursor.fetchone()

            api.send_direct_message('906078704', result[0] )
    
            api.send_direct_message('906078704', "salut")
    

def botRoutine(api):

    now = datetime.now().time()
    current_time = now.strftime("%H:%M:%S")
    while (True):
        if current_time == "19:00":
            api.update_status("""random_text_generated""")


if __name__ == "__main__":
    auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_KEY, credentials.ACCESS_SECRET)
    api = tweepy.API(auth)

    connection = pymysql.connect(host=credentials.JaHost,
                             user=credentials.JaUser,
                             password=credentials.JaPwrd,
                             database=credentials.JaName)

    senddmtest(api, connection)
    now = datetime.now().time()
    current_time = now.strftime("%H:%M")
    print(current_time == "18:00")
    ##publishTweetFromInput(api)
    connection.close()




