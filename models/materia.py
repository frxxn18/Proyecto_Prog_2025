class Materia:
    def __init__(self, id: int, nombre: str, departamento: str):
        self.id = id
        self.nombre = nombre
        self.departamento = departamento

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Departamento: {self.departamento}"
