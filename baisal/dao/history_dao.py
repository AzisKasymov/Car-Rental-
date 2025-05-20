from dao.BaseDao import Dao
import sys

sys.path.append("/Users/argenkulzhanov/Desktop/Designer/baisal/classes")
from classes.history import History

class HistoryDAO(Dao):
    def __init__(self, db_path):
        super().__init__(db_path)

    def insert(self, history: History):
        query = "INSERT INTO History (user_name, car_model, pickup_address, return_address,start_datetime, end_datetime,total_price) VALUES (?, ?, ?, ?,?,?,?)"
        self._cursor.execute(query, (history.get_username(), history.get_car_model(), history.get_pickup_address(), history.get_return_address(), history.get_start_datetime(), history.get_end_datetime(), history.get_total_price()))
        self._connection.commit()

    def get_history_by_user_id(self, user_id):
        query = "SELECT * FROM history WHERE user_id = ?"
        self._cursor.execute(query, (user_id,))
        rows = self._cursor.fetchall()
        histories = []
        for row in rows:
            history = History(row[1], row[2], row[3], row[4])
            histories.append(history)
        return histories