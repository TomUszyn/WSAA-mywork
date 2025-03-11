from flask import Flask, request

app = Flask(__name__)
#app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "Hello. Welcome to my rest server."

# Show all staff
@app.route('/staff', methods=['GET'])
def getall():
    return "All staff"

# Find by id
@app.route('/staff/<int:id>', methods=['GET'])
def findbyid(id):
    return "find by id"

# Create new staff menber
@app.route('/staff', methods=['POST'])
def create():
    # read json from the body
    jsonstring = request.json
    return f"create {jsonstring}"

# Update staff member by id
@app.route('/staff/<int:id>', methods=['PUT'])
def update(id):
    jsonstring = request.json
    return f"update {id} {jsonstring}"

# Delete staff member by id
@app.route('/staff/<int:id>', methods=['DELETE'])
def delete(id):
    return f"delete {id}"

if __name__ == "__main__":
    app.run(debug=True)