from db.db_conection import DBConection
from db.admin_consulta import adminConsulta
from service import admin_service


def main():
    cone = DBConection().get_conection()

    admin_consulta = adminConsulta(cone)
    admin_servic = admin_service.AdminService(admin_consulta)

    #admin_servic.create_courses("3ro", "D")

    admin_servic.create_subject("Math")

    

if __name__ == "__main__":
    main()