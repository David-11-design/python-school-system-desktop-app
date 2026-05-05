class adminConsulta:

    def __init__(self, conection):
        self.conection = conection
    #Query admin identify
    def validate_admin(self, username):
        try:
            cursor = self.conection.cursor()
            cursor.execute("Select * from admin where username =?", (username,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error fetching teacher by username: {e}")
            return None

    def validate_teacher(self, username):
        try:
            cursor = self.conection.cursor()
            cursor.execute("Select * from teachers where username =?", (username,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error fetching teacher by username: {e}")
            return None
        
    def create_teacher(self, name, fullname, username, password):
        try:
            cursor = self.conection.cursor()
            cursor.execute("Select * From teachers where name = ? and fullname = ?", (name, fullname))
            if cursor.fetchone():
                return False
            cursor.execute("INSERT INTO teachers (name, fullname, username, password) values (?, ?, ?, ?)", (name, fullname, username, password))
            self.conection.commit()
            return True

        except Exception as e:
            print(f"Error creating teacher: {e}")
            return False
    
    def create_course(self, name, parallel):
        try:
            cursor = self.conection.cursor()
            cursor.execute("INSERT INTO courses (name, parallel) values (?, ?)", (name, parallel))
            self.conection.commit()
            return True
        except Exception as e:
            print(f"Error creating course: {e}")

    def create_subjecta(self, name):
        try:
            cursor = self.conection.cursor()
            cursor.execute("INSERT INTO subjects (name) values (?)", (name,))
            self.conection.commit()
            return True
        except Exception as e:
            print(f"Error creating subject: {e}")

    def all_teacher(self):
        try:
            cursor = self.conection.cursor()
            cursor.execute("SELECT * FROM teachers")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching teachers: {e}")
            return []
    
    def all_courses(self):
        try:
            cursor = self.conection.cursor()
            cursor.execute("SELECT * FROM courses")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error fetching courses: {e}")
            return []
    
    def link_teacher_course(self, teacher_id, course_id):
        try:
            cursor = self.conection.cursor()
            cursor.execute("INSERT INTO teacher_courses (teacher_id, course_id) values (?, ?)", (teacher_id, course_id))
            self.conection.commit()
            return True
        except Exception as e:
            print(f"Error linking teacher to course: {e}")
            return False