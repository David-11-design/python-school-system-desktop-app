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
    conexion.commit()

except sqlite3.Error as e:
    print(f"Error connecting to database: {e}")
finally:
    conexion.close()