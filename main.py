import warnings
warnings.filterwarnings(
    "ignore",
    message="sipPyTypeDict.*",
    category=DeprecationWarning
)
import sys
import sqlite3
from PyQt5 import QtWidgets
from f.car1_ui import Ui_MainWindow
from classes.mc.controller import Controller


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Скрыть таббар и кнопку "List of cars"
        self.tabWidget.tabBar().hide()
        self.listB.hide()

        self.ctrl = Controller()

        # Создание таблиц в базе данных
        conn = sqlite3.connect('cars.db')
        conn.execute('PRAGMA journal_mode=WAL;')
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                is_admin INTEGER NOT NULL DEFAULT 0
            );
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Cars (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                make TEXT NOT NULL,
                model TEXT NOT NULL,
                name TEXT NOT NULL,
                price REAL NOT NULL
            );
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS Rentals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                car_id INTEGER NOT NULL,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                returned INTEGER NOT NULL DEFAULT 0
            );
        """)
        conn.commit()
        conn.close()

        # Начать с экрана входа, отключить кнопки навигации
        self.tabWidget.setCurrentWidget(self.log_page)
        for btn in (self.addB, self.editB, self.searchB_3, self.profileB):
            btn.setEnabled(False)

        # Кнопки навигации
        self.loginB.clicked.connect(self.login_user)
        for field in (self.name_in, self.email_in, self.password_in):
            field.returnPressed.connect(self.login_user)
        self.logoutB.clicked.connect(self.logout_user)
        self.addB.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.add_page))
        self.editB.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.edit_page))
        self.searchB_3.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.playlist_page))
        self.profileB.clicked.connect(lambda: self.tabWidget.setCurrentWidget(self.profile_page))

        # Действия с машинами
        self.saveB_1.clicked.connect(self.add_car)      # Сохранить на вкладке "Добавить машину"
        self.searchB.clicked.connect(self.search_car)   # Поиск на вкладке "Редактирование машины"
        self.saveB_3.clicked.connect(self.update_car)   # Сохранить на вкладке "Редактировать машину"
        self.deleteB.clicked.connect(self.delete_car)   # Удалить машину

        # Плейлист и бронирование (заглушки)
        self.searchB_4.clicked.connect(self.search_page)
        self.bookB.clicked.connect(self.book_rental)

    def enable_nav(self, enable=True):
        for btn in (self.addB, self.editB, self.searchB_3, self.profileB):
            btn.setEnabled(enable)

    def load_table(self):
        cars = self.ctrl.list_cars()
        table = self.search_table
        table.setRowCount(len(cars))

        for i, car in enumerate(cars):
            table.setItem(i, 0, QtWidgets.QTableWidgetItem(car.type))
            table.setItem(i, 1, QtWidgets.QTableWidgetItem(car.model))
            table.setItem(i, 2, QtWidgets.QTableWidgetItem(car.name))
            table.setItem(i, 3, QtWidgets.QTableWidgetItem(f"{car.price:.2f}"))

    def show_list(self):
        """Метод для отображения всех машин в таблице Search"""
        self.tabWidget.setCurrentWidget(self.search_page)

        self.load_table()  # Загружаем данные в таблицу

    def search_car(self):
        key = self.car_search.text().strip()  # Получаем ключ для поиска
        if not key:
            QtWidgets.QMessageBox.warning(self, "Error", "Enter ID or name")
            return

        # Получаем все машины из базы данных
        cars = self.ctrl.list_cars()

        # Фильтруем автомобили по ключу
        filtered_cars = [car for car in cars if key.lower() in car.name.lower() or key.lower() in car.model.lower()]

        # Обновляем таблицу
        table = self.search_table  # Используем search_table для отображения
        table.setRowCount(len(filtered_cars))  # Обновляем количество строк в таблице

        for i, car in enumerate(filtered_cars):
            table.setItem(i, 0, QtWidgets.QTableWidgetItem(car.type))   # Тип
            table.setItem(i, 1, QtWidgets.QTableWidgetItem(car.model))  # Модель
            table.setItem(i, 2, QtWidgets.QTableWidgetItem(car.name))   # Название
            table.setItem(i, 3, QtWidgets.QTableWidgetItem(f"{car.price:.2f}"))  # Цена

    def login_user(self):
        name = self.name_in.text().strip()
        email = self.email_in.text().strip()
        password = self.password_in.text().strip()
        if name and email and password:
            # Попытка зарегистрироваться (игнорировать, если уже существует)
            try:
                self.ctrl.handle_add_user(name, email, password)
                self.name_in.clear()
            except Exception:
                pass
        user = self.ctrl.handle_user_login(email, password)
        if user:
            self.current_user = user
            label = user.name or user.email
            self.user_label.setText(f"Welcome {label}!")
            for btn in (self.addB, self.editB, self.searchB_3, self.profileB):
                btn.setEnabled(True)
            self.populate_profile()
            self.tabWidget.setCurrentWidget(self.profile_page)
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "Invalid credentials")

    def logout_user(self):
        for btn in (self.addB, self.editB, self.searchB_3, self.profileB):
            btn.setEnabled(False)
        self.tabWidget.setCurrentWidget(self.log_page)

    def add_car(self):
        car_type = self.box_add_1.currentText()
        model = self.name_in_1.text().strip()
        price_txt = self.price_in_1.text().strip()
        if not (model and price_txt):
            QtWidgets.QMessageBox.warning(self, "Error", "Model and Price required")
            return
        try:
            price = float(price_txt)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Error", "Price must be a number")
            return
        cid = self.ctrl.add_car(car_type, model, model, price)
        QtWidgets.QMessageBox.information(self, "Success", f"Added car ID={cid}")
        self.name_in_1.clear()
        self.price_in_1.clear()

    def search_page(self):
        QtWidgets.QMessageBox.information(self, "Info", "Car search not implemented yet")

    def book_rental(self):
        QtWidgets.QMessageBox.information(self, "Info", "Book rental not implemented yet")

    def populate_profile(self):
        user = self.current_user
        table = self.profile_table
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(['ID', 'Name', 'Email', 'Admin'])
        table.setRowCount(1)
        table.setItem(0, 0, QtWidgets.QTableWidgetItem(str(user.id)))
        table.setItem(0, 1, QtWidgets.QTableWidgetItem(user.name))
        table.setItem(0, 2, QtWidgets.QTableWidgetItem(user.email))
        table.setItem(0, 3, QtWidgets.QTableWidgetItem(str(user.is_admin)))

    def update_car(self):
        if not hasattr(self, 'current_car_id'):
            QtWidgets.QMessageBox.warning(self, "Error", "Select a car first")
            return
        car_type = self.box_edit_1.currentText()
        model = self.name_in_4.text().strip()
        price_txt = self.price_in_2.text().strip()
        if not (model and price_txt):
            QtWidgets.QMessageBox.warning(self, "Error", "Model and Price required")
            return
        try:
            price = float(price_txt)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Error", "Price must be a number")
            return
        self.ctrl.update_car(self.current_car_id, type_=car_type, model=model, name=model, price=price)
        QtWidgets.QMessageBox.information(self, "Success", "Car updated")

    def delete_car(self):
        if not hasattr(self, 'current_car_id'):
            QtWidgets.QMessageBox.warning(self, "Error", "Select a car first")
            return
        if QtWidgets.QMessageBox.question(self, "Confirm", "Delete this car?") == QtWidgets.QMessageBox.Yes:
            self.ctrl.delete_car(self.current_car_id)
            QtWidgets.QMessageBox.information(self, "Success", "Car deleted")



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
