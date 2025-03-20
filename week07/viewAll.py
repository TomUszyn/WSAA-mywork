import mysql.connector
import dbconfig as cfg

connection = mysql.connector.connect(
  host=       cfg.mysql['host'],
  user=       cfg.mysql['user'],
  password=   cfg.mysql['password'],
  database=   cfg.mysql['database']
)

mycursor = connection.cursor()
sql = "select * from students"  
#mycursor.execute(sql)
mycursor.execute(sql)
result = mycursor.fetchall()
for x in result:
 print(x)

mycursor.close()
connection.close()