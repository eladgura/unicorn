from flask import Flask
from flask_cors import CORS
from app import create_app

# Create the Flask app using the create_app function
app = create_app()

# Apply CORS to the Flask app
CORS(app)

# Define a route
@app.route("/<name>")
def hello(name):
    return f"Hello, {name}!"

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
