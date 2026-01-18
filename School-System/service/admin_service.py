class AdminService:

    def __init__(self, admin_consulta):
        # Dependency Injection
        self.admin_consulta = admin_consulta
    
    def login(self, username, password):
        
        if not username or not password:
            return False
        
        admin = self.admin_consulta.get_by_username(username)

        if not admin:
            return False
        
        if password != admin[4]:
            return True
        
        return True
    
    def create_teacher_service(self, name, fullname, username, password):
        if not name or not fullname or not username or not password:
            print("Fields are required")
            return False

        if isinstance(name, str) and isinstance(fullname, str) and isinstance(username, str) and isinstance(password, str):
            if self.admin_consulta.create_teacher(name, fullname, username, password):
                print("User created successfully")
            else:
                print("User could not be created")
        else:
            print("The fields must be strings")

    def create_courses(self, name, parallel):
        if not name or not parallel:
            print("Fields are required")
            return False
        
        vowels_parallels = ["A","B","C"]

        if isinstance(name, str) and (isinstance(parallel, str) and parallel in vowels_parallels):
            if self.admin_consulta.create_course(name, parallel):
                print("The course was created successfully")
            else:
                print("The course could not be created")
        else:
            print("the fields 'name and parallel' must be string and parallel must be A, B, or C")

    def create_subject(self, name):
        if not name:
            print("The field 'name' is required")
        
        if isinstance(name, str):
            if self.admin_consulta.create_subject(name):
                print("The subject was created successfully")
            else:
                print("The subject could not be created")
        else:
            print("The field 'name' must be a string")