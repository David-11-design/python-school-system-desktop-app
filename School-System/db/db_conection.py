import sqlite3

try:
    #Conection
    conexion = sqlite3.connect('db.db')

    cursor = conexion.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS admin(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   fullname TEXT NOT NULL,
                   username TEXT NOT NULL,
                   password TEXT NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS teachers(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   fullname TEXT NOT NULL,
                   username TEXT NOT NULL,
                   password TEXT NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS students(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   fullname TEXT NOT NULL,
                   age INTEGER NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS courses(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   parallel TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS subjects(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS notes(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   student_id INTEGER NOT NULL,
                   subject_id INTEGER NOT NULL,
                   note REAL NOT NULL,
                   FOREIGN KEY(student_id) REFERENCES students(id),
                   FOREIGN KEY(subject_id) REFERENCES subjects(id))''')

    conexion.commit()

except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")
finally:
    conexion.close()
