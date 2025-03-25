# flask server that links to a DAO
# author: Tomasz Uszynski


from flask import Flask, jsonify, request
from studentDAO import StudentDAO  # Importing the DAO

app = Flask(__name__)

# Get all students
@app.route('/students', methods=['GET'])
def get_all_students():
    students = StudentDAO.getAll()
    return jsonify(students)

# Get a student by ID
@app.route('/students/<int:id>', methods=['GET'])
def get_student_by_id(id):
    student = StudentDAO.findByID(id)
    if student:
        return jsonify(student)
    return jsonify({"error": "Student not found"}), 404

# Create a new student
@app.route('/students', methods=['POST'])
def create_student():
    data = request.json
    if not data or not all(key in data for key in ["name", "age", "course"]):
        return jsonify({"error": "Invalid request, missing data"}), 400
    
    new_student = StudentDAO.create(data)
    return jsonify(new_student), 201

# Update a student
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.json
    if not data or not all(key in data for key in ["name", "age", "course"]):
        return jsonify({"error": "Invalid request, missing data"}), 400
    
    if not StudentDAO.findByID(id):
        return jsonify({"error": "Student not found"}), 404
    
    StudentDAO.update(id, data)
    return jsonify({"message": "Student updated successfully"}), 200

# Delete a student
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    if not StudentDAO.findByID(id):
        return jsonify({"error": "Student not found"}), 404
    
    StudentDAO.delete(id)
    return jsonify({"message": "Student deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
