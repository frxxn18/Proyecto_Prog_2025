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
        nombre = data.get("nombre", "No definido")
        contraseña = data.get("contraseña", "No definido")
        if nombre is None:
            raise ValueError("Falta campo obligatorio (Nombre)")
        return Usuario(nombre, contraseña)
