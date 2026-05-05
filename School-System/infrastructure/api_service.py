import requests as req

class ApiClient:
    def __init__(self):
        self.base_url = "http://127.0.0.1:8000/students/"
    
    def login(self, username, password):
        url = f"{self.base_url}"
        
        data = {
            "username": username,
            "password": password
        }

        try:
            response = req.post(url, json=data)
            return response.json()
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def create_teacher(self, name, fullname, username, password):
        url = "http://127.0.0.1:8000/create-teacher/"

        data = {
            "name": name,
            "fullname": fullname,
            "username": username,
            "password": password
        }

        try:
            response = req.post(url, json=data)
            return response.json()
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    
    def CreateCourseAdmin(self, name, parallel):
        url = "http://127.0.0.1:8000/Create-Course/"

        data = {
            "name": name,
            "parallel": parallel
        }
        try:
            response = req.post(url, json=data)
            return response.json()
        except Exception as e:
            print(f"An error occurred: {e}")
            return None