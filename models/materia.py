class Materia:
    def __init__(self, id: int, nombre: str, departamento: str):
        self.id = id
        self.nombre = nombre
        self.departamento = departamento

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Departamento: {self.departamento}"
    
    @staticmethod
    def from_dict(data):
        return Materia(
            id = data["id"],
            nombre = data["nombre"],
            departamento =data["departamento"]
        )

    @staticmethod
    def from_dict(data):
        id_ = data.get("id", "No definido")
        nombre = data.get("nombre", "No definido")
        departamento = data.get("departamento", "No definido")

        if id_ is None or nombre is None:
            raise ValueError("Faltan campos obligatorios")
        if "departamento" not in data:
            print(f"Materia {id_} no tiene departamento, se le asignara --> No definido ")
        
        return Materia(
            id = id_,
            nombre = nombre,
            departamento = departamento
        )