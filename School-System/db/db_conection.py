import sqlite3
import os

class DBConection:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "db.db")
        self.conection = sqlite3.connect(db_path)

    def get_conection(self):
        return self.conection
    
    def Scripts_Tables(self):
        try:
            cursor = self.conextion.cursor()

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
                   estudiante_id INTEGER NOT NULL,
                   subject_id INTEGER NOT NULL,
                   note1 INTEGER NULL,
                   note2 INTEGER NULL,
                   note3 INTEGER NULL,
                   note4 INTEGER NULL,
                   leccion INTEGER NULL,
                   examen INTEGER NULL,
                   FOREIGN KEY (estudiante_id) REFERENCES students(id),
                   FOREIGN KEY (subject_id) REFERENCES subjects(id))''')
            #Relationship Models 
            cursor.execute('''CREATE TABLE IF NOT EXISTS teacher_courses(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    teacher_id INTEGER NOT NULL,
                    course_id INTEGER NOT NULL,
                    FOREIGN KEY (teacher_id) REFERENCES teacher(id),
                    FOREIGN KEY (course_id) REFERENCES courses(id))''')

            cursor.execute('''CREATE TABLE IF NOT EXISTS course_subjects(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    course_id INTEGER NOT NULL,
                    subject_id INTEGER NOT NULL,
                    FOREIGN KEY (course_id) REFERENCES courses(id),
                    FOREIGN KEY (subject_id) REFERENCES subjects(id))''')
    

            cursor.commit()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

