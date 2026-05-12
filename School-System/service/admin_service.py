import random, re

class AdminService:

    def __init__(self, api_client):
        # Dependency Injection
        self.api_client = api_client
    
    def login(self, username, password):
        
        if not username or not password:
            return False
        
        user = self.api_client.login(username, password)

        if not user:
            return False

        if user.get("user_type") == "admin":
            return "admin"
        
        if user.get("user_type") == "teacher":
            return "teacher"
        
        return False

    def createTeacherService(self, name, fullname):
        if not name or not fullname:
            return False

        if isinstance(name, str) and isinstance(fullname, str):

            username = "".join([name, fullname]).lower().strip()

            password = ""

            for i in range(4):
                numbers = random.choice(range(0,10))
                password += str(numbers)

            if self.api_client.create_teacher(name, fullname, username, password):
                return True
            else:
                print("User could not be created")
                return False
        else:
            print("The fields must be strings")

    def create_course_service(self, name, parallel):
        if not name or not parallel:
            print("Fields are required")
            return "Empty field"
        
        vowels_parallels = ["A","B","C"]

        if (isinstance(name, str) and (isinstance(parallel, str)) and parallel in vowels_parallels):
            
            response = self.api_client.CreateCourseAdmin(name, parallel)

            if "error_empty" in response:
                return "Empty field"
            elif "error_exists" in response:
                return "Course already exists"
            else:
                return True
            """
            if self.api_client.CreateCourseAdmin(name, parallel):
                return True
            else:
                return False
            """
        else:
            return "Invalid parallel"

    def create_subject(self, name):
        if re.search(r"[^a-zA-Z ]", name): 
            return False
        
        if self.admin_consulta.create_subjecta(name):
            return "Created"
        else:
            return False
        
    def get_all_teacher_service(self):
        teacher_list = []

        for teacher in self.admin_consulta.all_teacher():
            diccionario = {"id": teacher[0],
                           "name": teacher[1],
                           "fullname": teacher[2]}
            teacher_list.append(diccionario)
        return teacher_list

    def get_all_course_service(self):
        course_list = []

        for course in self.admin_consulta.all_courses():
            diccionario = {"id": course[0],
                           "name": course[1],
                           "parallel": course[2]}
            course_list.append(diccionario)
        return course_list

    def assign_teacher_courses(self, teacher_ui, course_ui):

        teacher_id = None
        course_id = None

        for teacher in self.admin_consulta.all_teacher():
            if f"{teacher[1]} {teacher[2]}" == teacher_ui:
                teacher_id = teacher[0]
                break
        
        for course in self.admin_consulta.all_courses():
            if f"{course[1]} {course[2]}" == course_ui:
                course_id = course[0]
                break
        
        if self.admin_consulta.link_teacher_course(teacher_id, course_id):
            return True
        else:
            return False