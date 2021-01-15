import pymysql.cursors
import connectDB
import random


def query_quote():
    with connectDB.connection:
         with connectDB.connection.cursor() as cursor:
            print(random_number())
            sql = "SELECT `citation` FROM bigardTwitterBot WHERE `id`="+ str(random_number())
            cursor.execute(sql)
            resultQuote = cursor.fetchone()
            cursor.close()
            connectDB.connection.close()

            quote = resultQuote[0]            
            return quote


def random_number():
     with connectDB.connection:
         with connectDB.connection.cursor() as cursor:
            sql1 = "SELECT COUNT(*) FROM bigardTwitterBot"
            cursor.execute(sql1)
            resultNum = cursor.fetchone()
            cursor.close()
            connectDB.connection.close()

            number_cols = resultNum[0]
            numrandom = random.randint(0, number_cols-1)
            return numrandom
    

