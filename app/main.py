from fastapi import FastAPI
import sqlite3

app = FastAPI()

# Connect to SQLite database (it will be created automatically if it doesn't exist.
conn = sqlite3.connect('requests_count.db', check_same_thread=False)
cursor = conn.cursor()

# Create table to store the count (run once)
cursor.execute("CREATE TABLE IF NOT EXISTS counter (id INTEGER PRIMARY KEY, count INTEGER)")
conn.commit()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Counter App!"}

@app.get("/count")
def get_count():
    # Increment count by 1 for each request
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
