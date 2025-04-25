import sqlite3
from classes.dao.baseDAO import BaseDAO
from classes.rental import Rental

class RentalDAO(BaseDAO):
    def __init__(self, db_file='cars.db'):
        super().__init__(db_file)

    def add_rental(self, user_id, car_id, start_date, end_date):
        conn = self.connect_db()
        c = conn.cursor()
        c.execute(
            "INSERT INTO Rentals(user_id, car_id, start_date, end_date, returned) VALUES(?,?,?,?,?)",
            (user_id, car_id, start_date, end_date, 0)
        )
        conn.commit()
        rid = c.lastrowid
        conn.close()
        return rid
    def get_rental_by_id(self, rental_id):
        conn = self.connect_db()
        c = conn.cursor()
        c.execute("SELECT rental_id, user_id, car_id, start_date, end_date, returned FROM Rentals WHERE rental_id = ?", (rental_id,))
        row = c.fetchone()
        conn.close()
        return Rental(*row) if row else None
    def get_rentals_by_user_id(self, user_id):
        conn = self.connect_db()
        c = conn.cursor()
        c.execute("SELECT rental_id, user_id, car_id, start_date, end_date, returned FROM Rentals WHERE user_id = ?", (user_id,))
        rows = c.fetchall()
        conn.close()
        return [Rental(*r) for r in rows]
    def get_all_rentals(self):
        conn = self.connect_db()
        c = conn.cursor()
        c.execute("SELECT rental_id, user_id, car_id, start_date, end_date, returned FROM Rentals")
        rows = c.fetchall()
        conn.close()
        return [Rental(*r) for r in rows]
    def update_rental(self, rental_id, **fields):
        conn = self.connect_db()
        c = conn.cursor()
        clause = ", ".join(f"{k} = ?" for k in fields)
        vals = list(fields.values()) + [rental_id]
        c.execute(f"UPDATE Rentals SET {clause} WHERE id = ?", vals)
        conn.commit()
        conn.close()
    def delete_rental_by_id(self, rental_id):
        conn = self.connect_db()
        c = conn.cursor()
        c.execute("DELETE FROM Rentals WHERE rental_id = ?", (rental_id,))
        conn.commit()
        conn.close()