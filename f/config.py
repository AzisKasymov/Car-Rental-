# config.py
import os

# Single source of truth for the SQLite file
DB_FILE = os.path.join(os.path.dirname(__file__), 'cars.db')
