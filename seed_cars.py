import sqlite3

cars = [
    # (type, model, name, price)
    ('SUV',     'Hyundai',  'Solaris',  2100.0),
    ('Crossover',   'Honda',  'Civic',  2200.0),
    ('Sedan','Lexus',  'RX',   4200.0),
    ('SUV',     'Hyundai',  'Avante',  1900.0),
    ('Sedan',   'Honda',  'CR-V',  2800.0),
    ('Crossover','Lexus',  'LX600',   5200.0),
]

conn = sqlite3.connect('cars.db')
c = conn.cursor()

c.execute("""
    CREATE TABLE IF NOT EXISTS Cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT NOT NULL,
        make TEXT NOT NULL,
        model TEXT NOT NULL,
        name TEXT NOT NULL,
        price REAL NOT NULL
    );
""")

c.executemany(
    "INSERT INTO Cars(type, make, model, name, price) VALUES (?, '', ?, ?, ?)",
    [(t, m, n, p) for (t, m, n, p) in cars]
)

conn.commit()
conn.close()
print(f"Inserted {len(cars)} cars.")
