import pymysql.cursors
import connectDB
import random


def query_quote():
    numrandom = 0
    quote = ""
    with connectDB.connection:
         with connectDB.connection.cursor() as cursor:

            sql1 = "SELECT COUNT(*) FROM bigardTwitterBot"
            cursor.execute(sql1)

            resultNum = cursor.fetchone()
            number_cols = resultNum[0]
            numrandom = random.randint(0, number_cols-1)

            sql = "SELECT `citation` FROM bigardTwitterBot WHERE `id`="+ str(numrandom)
            cursor.execute(sql)
            
            resultQuote = cursor.fetchone()
            quote = resultQuote[0]
            cursor.close()
            connectDB.connection.close()
    return quote
    

