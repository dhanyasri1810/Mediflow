
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
from pathlib import Path

app = Flask(__name__)
CORS(app)

DB_PATH = Path(__file__).with_name("mediflow.db")


def get_db():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    with get_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_name TEXT NOT NULL,
                department TEXT NOT NULL,
                appointment_date TEXT NOT NULL,
                reason TEXT NOT NULL
            )
        """)


@app.route("/")
def home():
    return jsonify({
        "project": "MediFlow",
        "status": "Backend running"
    })


@app.route("/appointments", methods=["POST"])
def book_appointment():
    data = request.get_json(silent=True) or {}

    name = str(data.get("patient_name", "")).strip()
    department = str(data.get("department", "")).strip()
    date = str(data.get("appointment_date", "")).strip()
    reason = str(data.get("reason", "")).strip()

    if not all([name, department, date, reason]):
        return jsonify({"error": "All fields are required"}), 400

    with get_db() as db:
        cursor = db.execute("""
            INSERT INTO appointments
            (patient_name, department, appointment_date, reason)
            VALUES (?, ?, ?, ?)
        """, (name, department, date, reason))

        appointment_id = cursor.lastrowid

    return jsonify({
        "message": "Appointment booked successfully",
        "appointment_id": appointment_id
    }), 201


@app.route("/appointments", methods=["GET"])
def list_appointments():
    with get_db() as db:
        rows = db.execute("""
            SELECT id, patient_name, department, appointment_date, reason
            FROM appointments ORDER BY id DESC
        """).fetchall()

    return jsonify([dict(row) for row in rows])


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
