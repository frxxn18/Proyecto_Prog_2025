from datetime import datetime

class Prestamo:
    def __init__(
        self,
        nie: str,
        curso: str,
        isbn: str,
        fecha_entrega: str,
        fecha_devolucion: str,
        estado: str = "P"
    ):
        self.nie = nie
        self.curso = curso
        self.isbn = isbn
        self.fecha_entrega = fecha_entrega
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado

    def __str__(self):
        return (
            f"NIE: {self.nie}, Curso: {self.curso}, ISBN: {self.isbn}, "
            f"Entrega: {self.fecha_entrega}, Devolución: {self.fecha_devolucion}, Estado: {self.estado}"
        )
    

    def to_dict(self):
        return {
            "nie": self.nie,
            "curso": self.curso,
            "isbn": self.isbn,
            "fecha_entrega": self.fecha_entrega,
            "fecha_devolucion": self.fecha_devolucion,
            "estado": self.estado
        }
    

    @staticmethod
    def from_dict(data: dict):
        estado = data.get
        if estado not in ["P", "D"]:
            estado = "P"
        return Prestamo(
            nie=data["nie"],
            curso=data["curso"],
            isbn=data["isbn"],
            fecha_entrega=data["fecha_entrega"],
            fecha_devolucion=data["fecha_devolucion"],
            estado= estado
        )
    

    def marcar_como_devuelto(self):
        self.estado = "D"