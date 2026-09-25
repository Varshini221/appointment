from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)

CORS(app)

def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/appointments", methods=["GET"])
def get_appointments():
    rows = db.execute("""
        SELECT a.id, a.date, a.cost, a.notes, s.name, s.category
        FROM appointments a
        JOIN services s ON a.service_id = s.id
        ORDER BY a.date
    """).fetchall()    
    return jsonify([dict(r) for r in rows])

