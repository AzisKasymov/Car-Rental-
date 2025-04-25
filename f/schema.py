# schema.py
import sqlite3
from config import DB_FILE

def init_db():
    """Create all tables if they don't already exist."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        user_id   INTEGER PRIMARY KEY AUTOINCREMENT,
        email     TEXT    NOT NULL UNIQUE,
        password  TEXT    NOT NULL,
        is_admin  INTEGER NOT NULL DEFAULT 0
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Cars (
        car_id   INTEGER PRIMARY KEY AUTOINCREMENT,
        type     TEXT    NOT NULL CHECK(type IN ('Crossover','SUV','Sedan')),
        make     TEXT    NOT NULL,
        model    TEXT    NOT NULL,
        name     TEXT    NOT NULL,
        price    REAL    NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Rentals (
        rental_id  INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id    INTEGER NOT NULL,
        car_id     INTEGER NOT NULL,
        start_date TEXT    NOT NULL,
        end_date   TEXT    NOT NULL,
        returned   INTEGER NOT NULL DEFAULT 0,
        FOREIGN KEY(user_id) REFERENCES Users(user_id),
        FOREIGN KEY(car_id)  REFERENCES Cars(car_id)
    );
    """)

    conn.commit()
    conn.close()
