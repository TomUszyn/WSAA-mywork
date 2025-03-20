import mysql.connector
import dbconfig as cfg

connection = mysql.connector.connect(
  host=       cfg.mysql['host'],
  user=       cfg.mysql['user'],
  password=   cfg.mysql['password'],
  database=   cfg.mysql['database']
)

mycursor = connection.cursor()
sql = "select * from students where id = %s"
values = (1,)

mycursor.execute(sql,values)
result = mycursor.fetchall()
for x in result:
 print(x)

mycursor.close()
connection.close()