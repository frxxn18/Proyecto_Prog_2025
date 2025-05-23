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
        nie = data.get("nie", "No definido")
        nombre = data.get("nombre", "No definido")
        apellidos = data.get("apellidos", "")
        tramo = data.get("tramo", 0)
        bilingüe = data.get("bilingüe", False)

        if nie is None:
            raise ValueError("Falta campo obligatorio nie")
        return Alumno(
            nie = nie,
            nombre = nombre,
            apellidos = apellidos,
            tramo = tramo,
            bilingüe = bilingüe
        )