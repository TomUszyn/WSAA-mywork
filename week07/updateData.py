import mysql.connector
import dbconfig as cfg

connection = mysql.connector.connect(
  host=       cfg.mysql['host'],
  user=       cfg.mysql['user'],
  password=   cfg.mysql['password'],
  database=   cfg.mysql['database']
)

mycursor = connection.cursor()
sql = "update students set name = %s, age = %s where id = %s"

values = ("John", 38, 1)
mycursor.execute(sql,values)

connection.commit()
print("update done")

mycursor.close()
connection.close()