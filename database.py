import sqlite3

DB_NAME = "clients.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE,
            full_name TEXT,
            phone TEXT
        )
    """)

    conn.commit()
    conn.close()


def user_exists(telegram_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM clients WHERE telegram_id = ?",
        (telegram_id,)
    )

    user = cursor.fetchone()

    conn.close()

    return user is not None


def add_user(telegram_id, full_name, phone):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO clients
        (telegram_id, full_name, phone)
        VALUES (?, ?, ?)
    """, (telegram_id, full_name, phone))

    conn.commit()
    conn.close()
