#import mysql.connector
#import mysql.connector
#import dbconfig as cfg
#
#
#
#db = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  password=""
#)
#
#cursor = db.cursor()
#
#cursor.execute("create DATABASE wsaa")
#
#db.close()
#cursor.close()
import mysql.connector
import dbconfig as cfg

connection = mysql.connector.connect(
  host=       cfg.mysql['host'],
  user=       cfg.mysql['user'],
  password=   cfg.mysql['password'],
  database=   cfg.mysql['database']
)
#  host="localhost",
#  user="root",
#  password=""
#)

mycursor = connection.cursor()

mycursor.execute("create DATABASE wsaaaa")

mycursor.close()
connection.close()