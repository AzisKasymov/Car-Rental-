import sqlite3
from classes.dao.baseDAO import BaseDAO
from classes.car import Car

class CarDAO(BaseDAO):
    def __init__(self, db_file='cars.db'):
        super().__init__(db_file)

    def add_car(self, type_, model, name, price):
        conn = self.connect_db()
        cursor = conn.cursor()
        # 'make' column stored as empty string
        cursor.execute(
            "INSERT INTO Cars(type, make, model, name, price) VALUES (?, ?, ?, ?, ?)",
            (type_, "", model, name, price)
        )
        conn.commit()
        car_id = cursor.lastrowid
        conn.close()
        return car_id

    def get_car_by_id(self, id):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, type, make, model, name, price FROM Cars WHERE id = ?", (id,)
        )
        row = cursor.fetchone()
        conn.close()
        return Car(*row) if row else None

    def get_all_cars(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, type, make, model, name, price FROM Cars"
        )
        rows = cursor.fetchall()
        conn.close()
        return [Car(*row) for row in rows]

    def update_car(self, id, **fields):
        conn = self.connect_db()
        cursor = conn.cursor()
        set_clause = ", ".join([f"{key} = ?" for key in fields.keys()])
        values = list(fields.values()) + [id]
        cursor.execute(f"UPDATE Cars SET {set_clause} WHERE id = ?", values)
        conn.commit()
        conn.close()

    def delete_car_by_id(self, id):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM Cars WHERE id = ?", (id,)
        )
        conn.commit()
        conn.close()

