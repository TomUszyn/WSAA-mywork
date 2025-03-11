# Simple flask server

# Import the Flask class from the flask module
from flask import Flask

# Create the application object
app = Flask(__name__) # Passes the name of the module to the Flask constructor

# Use the decorator pattern to link the view function to a url (mapping)
@app.route("/") # The route() decorator tells Flask what URL should trigger the function

# Define the view using a function, which returns a string
def hello_world():
    return "Hello, World! I am a Flask server"

@app.route("/welcome")
def welcome():
    return "Welcome to Flask"

# Start the development server using the run() method
# Only run the app if the script is executed directly
if __name__ == "__main__":
    app.run(debug=True) # The run() method of the Flask class runs the application on the local development server    