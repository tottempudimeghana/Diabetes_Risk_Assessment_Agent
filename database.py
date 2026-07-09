import sqlite3

def create_database():
    conn = sqlite3.connect("diabetes.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        pregnancies INTEGER,
        glucose REAL,
        blood_pressure REAL,
        skin_thickness REAL,
        insulin REAL,
        bmi REAL,
        diabetes_pedigree REAL,
        age INTEGER,
        prediction TEXT,
        probability REAL,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


create_database()