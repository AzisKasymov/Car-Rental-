# classes/dao/userDAO.py
import sqlite3
from classes.dao.baseDAO import BaseDAO
from classes.user import User

class UserDAO(BaseDAO):
    def __init__(self, db_file="cars.db"):       # ← same DB
        super().__init__(db_file)

    def add_user(self, name, email, password, is_admin=False):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Users (name, email, password, is_admin) VALUES (?, ?, ?, ?)",
            (name, email, password, is_admin)
        )
        conn.commit()
        user_id = cursor.lastrowid             # ← fetch new ID
        conn.close()
        return user_id                         # ← return it

    def get_user_by_email(self, email):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, email, password, is_admin FROM Users WHERE email = ?", (email,))
        row = cursor.fetchone()
        conn.close()
        return User(*row) if row else None
