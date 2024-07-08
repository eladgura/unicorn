from app import create_app, db
from flask_cors import CORS
app = create_app()
CORS(app)
print("Hello, World!")
