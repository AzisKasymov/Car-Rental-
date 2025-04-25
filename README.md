

---

## **Project title: Car Renatal System**
## **Project Description:**
This project is a **Car Rental System** that enables users to view available cars, book rentals, and manage their account details. The system differentiates between regular users and admins, with admins having additional privileges to manage cars and view all rentals.

The system is designed using the **Model-View-Controller (MVC)** architecture, which helps maintain clean separation of concerns. The backend uses an SQLite database (`car.db`) to store user, car, and rental information.

---

## **Project Requirements List:**

### **User Management**
- **User Types**: There are two types of users in the system:
  - **Regular Users**: Can register, log in, view available cars, and make bookings.
  - **Admins**: Have additional privileges to manage cars (add, edit, delete) and view all rental transactions.

- **Authentication**:
  - Users can register for an account with an email and password.
  - Admins can access the admin panel to manage cars and view rental history.

### **Car Management**
- **Admin Privileges**: Admins can manage the car inventory. This includes:
  - Adding new cars to the system.
  - Editing car details (e.g., changing price or model).
  - Removing cars from the system.

- **Car Details**:
  - Each car has associated details such as **type** (e.g., SUV, Sedan), **model**, **name**, and **price** (rental cost).

### **Rental Management**
- **Booking**: Users can book cars for specified time periods.
- **Return Status**: Both users and admins can mark cars as returned once they are returned.
- **Rental History**: Users can view their past rentals, and admins can see all rental transactions across all users.

---

## **System Architecture**

This system follows the **Model-View-Controller (MVC)** pattern to structure the application. 

### **Model**
- The **Model** represents the data layer. It interacts with the database through **Data Access Objects (DAO)**. The system uses three key DAO classes:
  - **UserDAO**: Handles CRUD (Create, Read, Update, Delete) operations for user accounts.
  - **CarDAO**: Manages car inventory data.
  - **RentalDAO**: Tracks rental transactions.

### **View**
- The **View** is the user interface (UI) where users interact with the system. This is yet to be developed but would include screens for:
  - Viewing available cars.
  - Booking cars.
  - Admin interface for managing car listings and rentals.

### **Controller**
- The **Controller** acts as the intermediary between the **Model** and the **View**. It handles the user input (e.g., booking a car, updating rental status) and updates the UI accordingly.

---
## **Team Members List:**
## **Zamirbek uulu Baisal**

## **Zainabidinov Saidislom**

## **Kasymov Azis**

## **Roles of Group Members:**
Zamirbek uulu Baisal – Frontend Designer & Full Stack Developer
Responsibilities:
Designed all UI layouts using Qt Designer (.ui files).
Implemented navigation logic between windows (sedan, crossover, SUV, login, reservation).
Connected UI elements with backend logic using PyQt5 slots and signals.
Maintained overall project structure and ensured modular coding standards.
Focus: Application interface, user interaction flow, and integration of GUI components with backend logic.

Zainabidinov Saidislom – Backend Developer & Database Specialist
Responsibilities:
Developed backend functionality including reservation logic and user management.
Designed and maintained the SQLite database schema for users and reservations.
Handled registration, login logic, and secure data storage.
Ensured consistency between data states and UI updates.
Focus: Backend functionality, database operations, data validation, and business logic.

Kasymov Azis – Documentation & Presentation Lead
Responsibilities:
Created the README file with project overview, setup instructions, and contribution guide.
Designed the project presentation for team and instructor evaluations.
Managed GitHub repository, including commits, project descriptions, and version control.
Assisted with light debugging and final testing before delivery.
Focus: Documentation, version control, communication, and final packaging of the project.


## **Database Design**

The system relies on an **SQLite** database (`car.db`), which is initialized through the `db_setup.py` script. The database contains three main tables:

1. **Users Table**
   - Stores information about users.
   - Columns: `id`, `email`, `password`, `is_admin`.
   
2. **Cars Table**
   - Stores details about available cars for rent.
   - Columns: `car_id`, `type`, `model`, `name`, `price`.
   
3. **Rentals Table**
   - Tracks rental transactions.
   - Columns: `rental_id`, `user_id`, `car_id`, `start_date`, `end_date`, `returned`.

---

## **Setup Instructions**

To get started with the Car Rental System, follow the steps below:

### **Prerequisites**
Ensure you have the following installed:
- **Python 3.x**
- **SQLite** (comes bundled with Python)
- **Flask or Django** (Optional for the backend if you are creating an API or UI)

### **Clone the Repository**
```bash
git clone https://github.com/yourusername/car-rental-system.git
cd car-rental-system
```

### **Install Dependencies**
If you're using Flask, install the required libraries:
```bash
pip install flask
```

### **Initialize the Database**
Run the `db_setup.py` script to create the SQLite database and initialize the necessary tables:
```bash
python db_setup.py
```

---

## **How It Works**

### **DAO Layer**
The DAO layer abstracts the database operations, offering a set of reusable methods to interact with the database. The main DAO classes are:
- **BaseDAO**: Provides basic methods for connecting to the SQLite database.
- **UserDAO**: Handles user-related operations like registration and login.
- **CarDAO**: Manages operations for the car inventory (CRUD).
- **RentalDAO**: Manages rental transactions, including booking, status update, and history.

### **Controller**
The controller communicates with the DAO layer and is responsible for the business logic. It handles:
- User actions (e.g., registering, booking cars).
- Admin actions (e.g., adding or removing cars).

### **Database Interaction**
The **SQLite** database stores all data, and operations like creating rentals, updating car availability, and user registration are all handled through the DAOs.

---

## **Future Improvements**

- **User Authentication**: Implement token-based authentication for enhanced security.
- **Payment Integration**: Add a payment gateway for processing rental transactions.
- **Mobile Support**: Develop a mobile-responsive version of the app or create a mobile app.
- **Advanced Reporting**: Generate detailed reports for admins, such as rental trends, car availability, and financial reports.

---

## **Conclusion**

The **Car Rental System** provides a fully functional backend for managing users, cars, and rental transactions. The system is built to be scalable, easy to maintain, and extendable for future features.

## **UML:**

```

@startuml

class Model {
    +add_user(name, email, password, is_admin)
    +get_user(user_id)
    +list_users()
    +authenticate_user(email, password)
    +add_car(type, model, name, price)
    +list_cars()
    +get_car(car_id)
    +search_cars(term)
    +update_car(car_id, type_, model, name, price)
    +delete_car(car_id)
    +book_rental(user_id, car_id, start_date, end_date)
    +list_rentals()
}

class CarDAO {
    +add_car(type_, model, name, price)
    +get_car_by_id(id)
    +get_all_cars()
    +update_car(id, **fields)
    +delete_car_by_id(id)
}

class UserDAO {
    +add_user(name, email, password, is_admin)
    +get_user_by_email(email)
}

class RentalDAO {
    +add_rental(user_id, car_id, start_date, end_date)
    +get_rental_by_id(rental_id)
    +get_rentals_by_user_id(user_id)
    +get_all_rentals()
    +update_rental(rental_id, **fields)
    +delete_rental_by_id(rental_id)
}

Model --> CarDAO
Model --> UserDAO
Model --> RentalDAO
CarDAO --> BaseDAO
UserDAO --> BaseDAO
RentalDAO --> BaseDAO

@enduml
```
