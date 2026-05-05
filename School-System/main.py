from service import admin_service
from infrastructure.api_service import ApiClient
from UI.login_view import LoginView
import tkinter as tk

def main():
    api_client = ApiClient()
    admin_servic = admin_service.AdminService(api_client)

    #admin_servic.create_courses("3ro", "D")

    root = tk.Tk()
    root.title("School System")
    root.geometry("1000x600")
    LoginView(admin_servic, root)
    root.mainloop()

    #admin_servic.create_teacher_service("Luz", "Maria")
    

if __name__ == "__main__":
    main()
