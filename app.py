from flask import Flask
from app import create_app
from flask_cors import CORS
app=Flask
CORS(app)

@app.route("/<name>")
def hello(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)
