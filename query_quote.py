import pymysql.cursors
import connectDB
import random


def query_quote():
    if connectDB.connection.open:
        with connectDB.connection:
            with connectDB.connection.cursor() as cursor:
                # Create a new record
                sql = "SELECT `citation` FROM bigardTwitterBot WHERE `id`="+ str(random_number)
                cursor.execute(sql)
                resultQuote = cursor.fetchone()
                quote = resultQuote[0]            
                return quote


def random_number():
    if connectDB.connection.open:
        with connectDB.connection:
            with connectDB.connection.cursor() as cursor:
                sql = "SELECT COUNT(*) FROM bigardTwitterBot"
                cursor.execute(sql)
                resultNum = cursor.fetchone()

                number_cols = resultNum[0]
                numrandom = random.randint(0, numrandom-1)
                return numrandom
    

