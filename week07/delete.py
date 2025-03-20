import mysql.connector
import dbconfig as cfg

connection = mysql.connector.connect(
 host=cfg.mysql['host'],
 user=cfg.mysql['user'],
 password=cfg.mysql['password'],
 database=cfg.mysql['database']
)

mycursor = connection.cursor()
sql = "delete from students where id = %s"
values = (3,)
mycursor.execute(sql,values)

connection.commit()
print("delete done")

mycursor.close()
connection.close()