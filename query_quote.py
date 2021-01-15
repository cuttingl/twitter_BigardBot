import pymysql.cursors
import connectDB
import random


def query_quote():
    with connectDB.connection:
        with connectDB.connection.cursor() as cursor:
            # Create a new record
            sql = "SELECT `citation` FROM bigardTwitterBot WHERE `id`=%d"
            cursor.execute(sql, (random_number()))
            result = cursor.fetchone()            
            return result


def random_number():
    with connectDB.connection:
        with connectDB.connection.cursor() as cursor:
            sql = "SELECT COUNT(*) FROM bigardTwitterBot"
            cursor.execute(sql)
            resultNum = cursor.fetchone()

            numrandom = random.randint(0, resultNum-1)
            return numrandom

