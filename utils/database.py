import sqlite3
from datetime import datetime

DB_NAME = "database.db"

def initialize_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            tag TEXT,
            urgency INTEGER,
            importance INTEGER,
            status TEXT DEFAULT 'to do',
            created_at TEXT DEFAULT (date('now')),
            updated_at TEXT DEFAULT (date('now'))
        )
    """)
    conn.commit()
    conn.close()

def add_task(title, tag, urgency, importance):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tasks (title, tag, urgency, importance, status)
        VALUES (?, ?, ?, ?, 'to do')
    """, (title, tag, urgency, importance))
    conn.commit()
    conn.close()

def get_tasks():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, title, tag, urgency, importance, status, created_at, updated_at
        FROM tasks
    """)
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "id": row[0],
            "title": row[1],
            "tag": row[2],
            "urgency": row[3],
            "importance": row[4],
            "status": row[5],
            "created_at": row[6],
            "updated_at": row[7],
        }
        for row in rows
    ]

def update_task_status(task_id, status):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tasks
        SET status = ?, updated_at = date('now')
        WHERE id = ?
    """, (status, task_id))
    conn.commit()
    conn.close()

def update_task_details(task_id, title, tag, urgency, importance):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tasks
        SET title = ?, tag = ?, urgency = ?, importance = ?, updated_at = date('now')
        WHERE id = ?
    """, (title, tag, urgency, importance, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
    """, (task_id,))
    conn.commit()
    conn.close()

def reset_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS tasks")
    conn.commit()
    conn.close()
    initialize_db()