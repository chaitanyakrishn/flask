from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL '/'
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the Flask application
if __name__ == '__main__':
    # Change host to '0.0.0.0' to make it accessible to all devices on the network
    app.run(debug=True)
