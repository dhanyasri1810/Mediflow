
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "project": "MediFlow",
        "message": "Welcome to MediFlow!",
        "status": "under development"
    })

if __name__ == "__main__":
    app.run(debug=True)
