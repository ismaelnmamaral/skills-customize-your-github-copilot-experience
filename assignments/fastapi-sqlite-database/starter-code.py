import sqlite3
from fastapi import FastAPI, HTTPException

app = FastAPI(title="FastAPI SQLite API")


def get_db_connection():
    conn = sqlite3.connect("items.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT
        )
        """
    )
    conn.commit()
    conn.close()


init_db()


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI SQLite API"}


@app.get("/items")
def get_items():
    conn = get_db_connection()
    rows = conn.execute("SELECT * FROM items").fetchall()
    conn.close()
    return [dict(row) for row in rows]


@app.post("/items")
def create_item(item: dict):
    title = item.get("title")
    description = item.get("description")

    if not title:
        raise HTTPException(status_code=400, detail="Title is required")

    conn = get_db_connection()
    cursor = conn.execute(
        "INSERT INTO items (title, description) VALUES (?, ?)",
        (title, description),
    )
    conn.commit()
    item_id = cursor.lastrowid
    conn.close()
    return {"id": item_id, "title": title, "description": description}
