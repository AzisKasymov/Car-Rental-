# baseDAO.py
import sqlite3

class BaseDAO:
    def __init__(self, db_file="cars.db"):       # ← unified DB name
        self.db_file = db_file

    def connect_db(self):
        return sqlite3.connect(self.db_file)
