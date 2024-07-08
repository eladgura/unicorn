from app import create_app
from flask_cors import CORS

app = create_app()
CORS(app)

@app.route("/<name>")
def hello(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)
