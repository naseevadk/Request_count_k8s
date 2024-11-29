"""
FastAPI Counter Application

This module contains a simple FastAPI application that counts the number
of requests made to the `/count` endpoint. The count is stored in a SQLite
database (`requests_count.db`).
"""

import sqlite3
from fastapi import FastAPI

app = FastAPI()

# Connect to SQLite database (it will be created automatically if it doesn't exist)
conn = sqlite3.connect('requests_count.db', check_same_thread=False)
cursor = conn.cursor()

# Create table to store the count (run once)
cursor.execute("CREATE TABLE IF NOT EXISTS counter (id INTEGER PRIMARY KEY, count INTEGER)")
conn.commit()

@app.get("/")
def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the FastAPI Counter App!"}

@app.get("/count")
def get_count():
    """
    Endpoint that increments and returns the request count.
    """
    cursor.execute("SELECT count FROM counter WHERE id = 1")
    row = cursor.fetchone()

    if row:
        count = row[0] + 1
        cursor.execute("UPDATE counter SET count = ? WHERE id = 1", (count,))
    else:
        count = 1
        cursor.execute("INSERT INTO counter (id, count) VALUES (1, 1)")

    conn.commit()

    return {"count": count}
