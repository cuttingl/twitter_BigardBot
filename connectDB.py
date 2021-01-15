import pymysql.cursors
import credentials

# Connect to the database
connection = pymysql.connect(host=credentials.JaHost,
                             user=credentials.JaUser,
                             password=credentials.JaPwrd,
                             database=credentials.JaName)