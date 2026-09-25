from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)

CORS(app)

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

#creates the table if it doesnt exist
def init_db():
    db = get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(30) NOT NULL,
        category VARCHAR(30) NOT NULL, 
        time TIME NOT NULL,
        cost DECIMAL(3, 2) DEFAULT 0, 
        date DATE NOT NULL
        )        
    """)
    db.commit()

init_db()


@app.route("/appointments", methods = ["POST"])
def add_appointments():
    data = request.json
    db = get_db()
    db.execute(
        "INSERT INTO appointments(name, category, time, cost, date) VALUES(?, ?, ?, ?, ?)",
        (data["name"], data["category"], data["time"], data["cost"], data["date"])
    )
    db.commit()
    return jsonify({"ok": True}), 201


if __name__ == "__main__":
    app.run(debug=True, port=5001)