from db.admin_consulta import adminConsulta
from service import admin_service
from db import db_conection
import sqlite3


cone = db_conection.conexion # type: sqlite3.Connection

admin_consulta = adminConsulta(cone)
admin_service = admin_service.AdminService(admin_consulta)

admin_service.create_teacher_service("David", "Arevalo", "johndoe", "password123")