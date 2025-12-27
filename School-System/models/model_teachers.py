from models.model_admin import Admin

class teachers(Admin):
    
    def __init__(self, id, name, fullname, username, password):
        super().__init__(id, name, fullname, username, password)