class Usuario:
    def __init__(self, nombre: str, contraseña: str):
        self.nombre = nombre
        self.contraseña = contraseña

    def __str__(self):
        return f"Usuario: {self.nombre}"

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "contraseña": self.contraseña
        }

    @staticmethod
    def from_dict(data):
        return Usuario(data["nombre"], data["contraseña"])
