import mydb

connectdb = mydb.connectDB()

mycursor = connectdb.cursor()

print(mycursor.execute("SHOW TABLES"))
