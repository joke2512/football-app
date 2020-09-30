import mysql.connector
import csv
"""
For DB init and data insertion
"""

mydb = mysql.connector.connect(
  host="football-db.cbjwwglbjbqg.eu-central-1.rds.amazonaws.com",
  user="joke2512",
  password="Ju76gw54b8",
  port="3306"
)
mycursor = mydb.cursor()
print(mydb)
mycursor.execute("CREATE DATABASE IF NOT EXISTS Football")
mycursor.execute("CREATE TABLE IF NOT EXISTS Football.Players (ID INTEGER, name VARCHAR(255), age INTEGER, nationality VARCHAR(255), club VARCHAR(255), photo VARCHAR(255), overall INTEGER, value INTEGER, position VARCHAR(255))")
mycursor.execute("DELETE FROM Football.Players")
mycursor.close()
with open('data.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',', quotechar='|')
    first = True
    for row in data:
        print(row[0])
        # First row is cvs info
        if not first:
            # cleanup value number
            if "M" in row[11]:
                value = row[11].replace("€", "").replace("M", "")
                if "." in value:
                    v1, v2 = value.split(".")
                    value = v1 + v2 + "00000"
                else:
                    value += "000000"
            elif "K" in row[11]:
                value = row[11].replace("€", "").replace("k", "")
                if "." in value:
                    v1, v2 = value.split(".")
                    value = v1 + v2 + "00"
                else:
                    value += "000"
            else:
                value = row[11].replace("€", "")
            # insert row into database
            sql = ("INSERT INTO Football.Players VALUES(%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s ,%s )")
            vals = (row[1], row[2], row[3], row[5], row[9], row[4], row[7], value, row[21])
            mycursor = mydb.cursor()
            mycursor.execute(sql, vals)
            mycursor.close()
        first = False
mycursor = mydb.cursor()
mycursor.execute("SELECT count(*) FROM Football.Players")
for row in mycursor:
    print(row)

mydb.commit()
mycursor.close()
mydb.close()