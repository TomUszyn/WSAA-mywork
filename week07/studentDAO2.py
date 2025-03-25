# StudentDAO.py
# Demonstration of a Data Access Object (DAO) for Student records.

import mysql.connector
import dbconfig as cfg

class StudentDAO:
    def __init__(self):
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']
        self.connection = None
        self.cursor = None

    def getcursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def getAll(self):
        cursor = self.getcursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()
        self.closeAll()
        
        return [self.convertToDictionary(result) for result in results]

    def findByID(self, id):
        cursor = self.getcursor()
        sql = "SELECT * FROM student WHERE id = %s"
        cursor.execute(sql, (id,))
        result = cursor.fetchone()
        self.closeAll()

        return self.convertToDictionary(result) if result else None

    def create(self, student):
        cursor = self.getcursor()
        sql = "INSERT INTO student (name, age, course) VALUES (%s, %s, %s)"
        values = (student["name"], student["age"], student["course"])
        cursor.execute(sql, values)
        self.connection.commit()

        student["id"] = cursor.lastrowid
        self.closeAll()
        return student

    def update(self, id, student):
        cursor = self.getcursor()
        sql = "UPDATE student SET name=%s, age=%s, course=%s WHERE id=%s"
        values = (student["name"], student["age"], student["course"], id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def delete(self, id):
        cursor = self.getcursor()
        sql = "DELETE FROM student WHERE id = %s"
        cursor.execute(sql, (id,))
        self.connection.commit()
        affected_rows = cursor.rowcount
        self.closeAll()
        return affected_rows > 0  # Returns True if a row was deleted

    def convertToDictionary(self, resultLine):
        if not resultLine:
            return None  # Handles case where result is None

        attkeys = ['id', 'name', 'age', 'course']
        return {attkeys[i]: resultLine[i] for i in range(len(attkeys))}

# Create an instance of StudentDAO
StudentDAO = StudentDAO()
