import tkinter as tk

class TeacherUi:
    def __init__(self, service, root):
        self.teacher_services = service
        self.root = root
        self.options_teacher()

    def options_teacher(self):
        self.frame = tk.Frame(self.root, bg="lightgray", width=1000, height=600)
        self.frame.pack(fill=tk.BOTH, expand=True)