import tkinter as tk
from tkinter import messagebox
from .admin_ui import AdminUi
from .teacher_ui import TeacherUi

class LoginView:
    def __init__(self, service, root):
        self.service = service
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root, bg="lightgray", width=1000, height=600)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.frame, text="Welcome to the Admin Panel", fg="blue")
        self.label.place(x=110, y=10)

        self.username = tk.Entry(self.frame, justify=tk.CENTER, width=25)
        self.username.place(x=110, y=50)

        self.password = tk.Entry(self.frame, show="*", justify=tk.CENTER, width=25)
        self.password.place(x=110, y=90)

        self.click_button = tk.Button(self.frame, text="Login", command=self.logi_admin, bg="Black", fg="White", width=14)
        self.click_button.place(x=130, y=130)
    
    def logi_admin(self):
        username = self.username.get()
        password = self.password.get()

        if self.service.login(username, password) == "admin":
            self.frame.destroy()
            AdminUi(self.service, self.root)
        elif self.service.login(username, password) == "teacher":
            self.frame.destroy()
            TeacherUi(self.service, self.root)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")