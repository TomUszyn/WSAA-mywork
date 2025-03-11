from flask import Flask, redirect, url_for

app = Flask(__name__, static_url_path='', static_folder='staticpages')

# mapping
@app.route('/')
def index():
    return "<h1> Hi there, welcome to the index page </h1>"

@app.route('/users', methods=["GET"])
def get_users():
    return "Getting all users."

@app.route('/users/<username>', methods=["GET"])
def get_user_byname(username):
    return f"Hello {username}. Welcome to your profile"

@app.route('/users/<int:id>', methods=["GET"])
def get_user_byid(id):
    return f"Your ID is {id}."

@app.route('/users/', methods=["POST"])
def create_user():
    return f"Creating a user."

@app.route('/users/', methods=["PUT"])
def update_user():
    return f"Updating a user."

@app.route('/invalid', methods=["GET"])
def testingredirecting():
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)