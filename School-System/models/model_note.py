class Note:

    def __init__(self, id, estudiante_id, materia_id, grade1, grade2, grade3, grade4, lection, exam):
        self.id = id
        self.estudiante_id = estudiante_id
        self.materia_id = materia_id
        self.nota1 = grade1
        self.nota2 = grade2
        self.nota3 = grade3
        self.nota4 = grade4
        self.leccion = lection
        self.examen = exam