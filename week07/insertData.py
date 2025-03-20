import mysql.connector
import dbconfig as cfg

connection = mysql.connector.connect(
  host=       cfg.mysql['host'],
  user=       cfg.mysql['user'],
  password=   cfg.mysql['password'],
  database=   cfg.mysql['database']
)

mycursor = connection.cursor()
sql = "insert into students (name, age) values (%s, %s)"
values = ("Joanna", 58)
mycursor.execute(sql,values)

connection.commit()
print("1 record inserted, ID:", mycursor.lastrowid)

mycursor.close()
connection.close()