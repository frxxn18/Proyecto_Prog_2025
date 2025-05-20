class Alumno:
    def __init__(self, nie, nombre,apellidos, tramo, bilingüe):
        self.nie = nie
        self.nombre = nombre
        self.apellidos = apellidos
        self.tramo = tramo
        self.bilingüe = bilingüe

    def to_dict(self):
        return {
            "nie": self.nie,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "tramo": self.tramo,
            "bilingüe": self.bilingüe
        }
    

    @staticmethod
    def from_dict(data):
        return Alumno(
            data["nie"],
            data["nombre"],
            data["apellidos"],
            data["tramo"],
            data["bilingüe"]
        )