import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class AdminUi:
    def __init__(self, service, root):
        self.service = service
        self.root = root
        self.options_admin()

    def options_admin(self):
        if hasattr(self, "frame"):
            self.frame.destroy()

        self.frame = tk.Frame(self.root, bg="lightgray", width=1000, height=600)
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.label = tk.Label(self.frame, text="Welcome to the Admin Panel", fg="blue")
        self.label.place(x=110, y=10)

        self.click_button = tk.Button(self.frame, text="Create TeacherS", command=self.create_teacher,bg="White", fg="Black", width=25, height=10)
        self.click_button.place(x=130, y=100)

        self.click_button = tk.Button(self.frame, text="Create Courses", command=self.create_courses ,bg="White", fg="Black", width=25, height=10)
        self.click_button.place(x=410, y=100)

        self.click_button = tk.Button(self.frame, text="Create Subjects", command=self.create_subject,bg="White", fg="Black", width=25, height=10)
        self.click_button.place(x=680, y=100)

        self.click_button = tk.Button(self.frame, text="All Teachers", command=self.link_teacher_course,bg="White", fg="Black", width=25, height=10)
        self.click_button.place(x=260, y=320)

    def create_teacher(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.root, bg="lightgray", width=1000, height=600)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.label = tk.Label(self.frame, text="Create Teacher", fg="blue")
        self.label.place(x=110, y=10)

        self.name = tk.Entry(self.frame, justify=tk.CENTER, width=25)
        self.name.place(x=110, y=50)

        self.fullname = tk.Entry(self.frame, justify=tk.CENTER, width=25)
        self.fullname.place(x=110, y=90)

        self.click_button = tk.Button(self.frame, text="Create", command=self.call_create_teacher, bg="Black", fg="White", width=14)
        self.click_button.place(x=130, y=130)

    def call_create_teacher(self):
            name = self.name.get()
            fullname = self.fullname.get()

            if self.service.createTeacherService(name, fullname):
                messagebox.showinfo("Success", "Teacher created successfully")
            else:
                messagebox.showerror("Error", "Teacher could not be created")
            
    def create_courses(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.root, bg="lightgray", width=1000, height=600)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.name_label = tk.Label(self.frame, text="Create Course", fg="blue")
        self.name_label.place(x=110, y=10)

        self.name = tk.Entry(self.frame, justify=tk.CENTER, width=25)
        self.name.place(x=110, y=50)

        self.parallel_label = tk.Label(self.frame, text="Parallel", fg="blue")
        self.parallel_label.place(x=110, y=90)

        self.parallel = tk.Entry(self.frame, justify=tk.CENTER, width=25)
        self.parallel.place(x=110, y=120)

        self.click_button = tk.Button(self.frame, text="Create", command=self.get_create_course, bg="Black", fg="White", width=14)
        self.click_button.place(x=130, y=160)
    
    def get_create_course(self):
        name = self.name.get()
        parallel = self.parallel.get()

        if not self.service.create_course_service(name, parallel):
            messagebox.showwarning("Fields are required")
        
        if self.service.create_course_service(name, parallel):
            messagebox.showinfo("Success", "Course created successfully")
        else:
            messagebox.showerror("Error", "Course could not be created")
        
    def create_subject(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.root, bg="lightgray", width=1000, height=600)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.subject_label = tk.Label(self.frame, text="Create Subject", fg="blue")
        self.subject_label.place(x=110, y=10)

        self.subject = tk.Entry(self.frame, justify=tk.CENTER, width=25)
        self.subject.place(x=110, y=50)

        self.click_button = tk.Button(self.frame, text="Create", command=self.get_create_subject, bg="Black", fg="White", width=14)
        self.click_button.place(x=130, y=160)
    
    def get_create_subject(self):
        subject = self.subject.get()

        if not subject:
            messagebox.showwarning("Fields are required")
            return 

        type_data = self.service.create_subject(subject)

        if type_data:
            if type_data == "Created":
                messagebox.showinfo("Success", "Subject created successfully")
            else:
                messagebox.showerror("Error", "Subject could not be created")
        else:
            messagebox.showwarning("Error", "Subject must be a string")
    
    def link_teacher_course(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.root, bg="lightgray", width=1000, height=600)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.btn_back = tk.Button(self.frame, text="Back", command=self.options_admin, bg="Black", fg="White", width=14 )
        self.btn_back.place(x=10, y=10)

        self.label = tk.Label(self.frame, text="All Teachers", fg="blue")
        self.label.place(x=110, y=10)

        teachers = self.service.get_all_teacher_service()

        teachers_names = [f"{teacher['name']} {teacher['fullname']}" for teacher in teachers]

        self.combo_teacher = ttk.Combobox(self.frame, values=teachers_names)
        self.combo_teacher.place(x=110, y=50)

        self.label = tk.Label(self.frame, text="All Courses", fg="blue")
        self.label.place(x=280, y=10)

        courses = self.service.get_all_course_service()

        courses_names = [f"{course['name']} {course['parallel']}" for course in courses]

        self.combo = ttk.Combobox(self.frame, values=courses_names)

        self.combo.place(x=280, y=50)

        self.click_button = tk.Button(self.frame, text="Assign", command=self.a, bg="Black", fg="White", width=14)
        self.click_button.place(x=110, y=90)

    def a(self):
        selected_teacher = self.combo_teacher.get()
        selected_course = self.combo.get()

        if not selected_teacher or not selected_course:
            messagebox.showwarning("Fields are required")
            return
        
        b = self.service.assign_teacher_courses(selected_teacher, selected_course)   

        if b:
            messagebox.showinfo("Success", "Teacher assigned to course successfully")
        else:
            messagebox.showerror("Error", "Teacher could not be assigned to course")
            