import mysql.connector
import dbconfig as cfg

class StudentDAO:
    connection = ""
    cursor = ''
    host = ''
    user = ''
    password = ''
    database = ''

    def __init__(self):
        # Initialize the database connection details from the config
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']

    def getcursor(self):
        """Create a database connection and return the cursor."""
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        """Close the database connection and cursor."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def create(self, values):
        """Insert a new student into the database."""
        cursor = self.getcursor()
        sql = "INSERT INTO student (name, age) VALUES (%s, %s)"
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

    def getAll(self):
        """Retrieve all students from the database."""
        cursor = self.getcursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()
        students = []
        for result in results:
            student = {'id': result[0], 'name': result[1], 'age': result[2]}  # Assuming your table has columns: id, name, age
            students.append(student)
        self.closeAll()
        return students

    def findByID(self, id):
        """Find a student by their ID."""
        cursor = self.getcursor()
        sql = "SELECT * FROM student WHERE id = %s"
        cursor.execute(sql, (id,))
        result = cursor.fetchone()
        student = None
        if result:
            student = self.convertToDictionary(result)  # Use   convertToDictionary to convert result to dictionary
        self.closeAll()
        return student


    def findByID(self, id):
        """Find a student by their ID."""
        cursor = self.getcursor()
        sql = "SELECT * FROM student WHERE id = %s"
        cursor.execute(sql, (id,))
        result = cursor.fetchone()
        student = None
        if result:
            student = {'id': result[0], 'name': result[1], 'age': result[2]}
        self.closeAll()
        return student

    def update(self, values):
        """Update a student's information."""
        cursor = self.getcursor()
        sql = "UPDATE student SET name = %s, age = %s WHERE id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def delete(self, id):
        """Delete a student by their ID."""
        cursor = self.getcursor()
        sql = "DELETE FROM student WHERE id = %s"
        cursor.execute(sql, (id,))
        self.connection.commit()
        self.closeAll()
        
   def convertToDictionary(self, resultLine):
    """Convert a result row into a dictionary with student attributes."""
        attkeys = ['id', 'name', 'age']
        student = {}
        currentkey = 0
        for attrib in resultLine:
            student[attkeys[currentkey]] = attrib
            currentkey += 1
        return student
              
# Example usage
studentDAO = StudentDAO()

# # Creating a new student
# new_student_id = studentDAO.create(("John Doe", 25))
# print(f"New student created with ID: {new_student_id}")
# 
# # Retrieving all students
# students = studentDAO.getAll()
# for student in students:
#     print(student)
# 
# # Finding a student by ID
# student = studentDAO.findByID(new_student_id)
# print(f"Student with ID {new_student_id}: {student}")
# 
# # Updating a student's information
# studentDAO.update(("John Smith", 26, new_student_id))
# 
# # Deleting a student by ID
# studentDAO.delete(new_student_id)
# 