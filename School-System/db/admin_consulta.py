class adminConsulta:

    def __init__(self, conection):
        self.conection = conection
    #Query admin identify
    def  get_by_username(self, usernname):
        cursor = self.conection.cursor()
        cursor.execute("Select * from admin where username =?", (usernname))
        return cursor.fetchone()
    
    def create_teacher(self, name, fullname, username, password):
        try:
            cursor = self.conection.cursor()
            cursor.execute("INSERT INTO teachers (name, fullname, username, password) values (?, ?, ?, ?)", (name, fullname, username, password))
            cursor.commit()
            return True
        except Exception as e:
            print(f"Error creating teacher: {e}")
            return False