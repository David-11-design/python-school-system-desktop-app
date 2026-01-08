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
            return False

        if type(name) is str or type(fullname) is str or type(username) is str or type(password) is str:
            self.admin_consulta.create_teacher(name, fullname, username, password)
            print("User creado con exito")
        else:
            print("No se pudo crear user")


