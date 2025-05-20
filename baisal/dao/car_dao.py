from dao.BaseDao import Dao
import sys

sys.path.append("/Users/argenkulzhanov/Desktop/Designer/baisal/classes")
from classes.car import Car

class CarDAO(Dao):
    def __init__(self, db_path):
        super().__init__(db_path)

    def insert(self, car: Car):
        query = "INSERT INTO Cars (model, car_class, price_per_day, amount) VALUES (?, ?, ?, ?)"
        self._cursor.execute(query, (car.get_model(), car.get_car_class(), car.get_price_per_day(), car.get_amount()))
        self._connection.commit()

    def get_price_by_model(self, model):
        query = "SELECT price_per_day FROM Cars WHERE model = ?"
        self._cursor.execute(query, (model,))
        row = self._cursor.fetchone()
        if row:
            return row[0]
        return None

    def minus_amount_by_model(self, model):
        query = "UPDATE Cars SET amount = amount - 1 WHERE model = ?"
        self._cursor.execute(query, (model,))
        self._connection.commit()