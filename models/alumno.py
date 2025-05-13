class Alumno:
    def __init__(self, nie, nombre, apellido, apellidos, tramo, bilingue):
        self.nie = nie
        self.nombre = nombre
        self.apellido = apellido
        self.apellidos = apellidos
        self.tramo = tramo
        self.bilingue = bilingue

    def to_dict(self):
        return {
            "nie": self.nie,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "apellidos": self.apellidos,
            "tramo": self.tramo,
            "bilingue": self.bilingue
        }
    

    @staticmethod
    def from_dict(data):
        return Alumno(
            data["nie"],
            data["nombre"],
            data["apellidos"],
            data["tramo"],
            data["bilingue"]
        )