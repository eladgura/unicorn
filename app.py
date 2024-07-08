from flask import Flask, escape
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
CORS(app)

# Define a simple model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    
    def __repr__(self):
        return f'<User {self.name}>'

# Define a route
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

# Create database tables
with app.app_context():
    db.create_all()

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
