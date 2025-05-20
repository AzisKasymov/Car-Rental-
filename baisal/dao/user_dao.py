from dao.BaseDao import Dao
import sys

sys.path.append("/Users/argenkulzhanov/Desktop/Designer/baisal/classes")
from classes.user import User

class UserDAO(Dao):
    def init(self, db_path):
        super().__init__(db_path)

    def insert(self, user: User):
        query = "INSERT INTO users (username, password) VALUES (?, ?)"
        self._cursor.execute(query, (user.get_username(), user.get_password()))
        self._connection.commit()

    def find_by_username(self, username):
        query = "SELECT * FROM Users WHERE username = ?"
        self._cursor.execute(query, (username,))
        row = self._cursor.fetchone()
        if row:
            return User(row[1], row[2])  # Assuming row[1] is username and row[2] is password
        return None

    def find_by_id(self, user_id):
        query = "SELECT * FROM Users WHERE id = ?"
        self._cursor.execute(query, (user_id,))
        row = self._cursor.fetchone()
        if row:
            return User(row[1], row[2])
        return None