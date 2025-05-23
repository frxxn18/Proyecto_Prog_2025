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
        nie = data.get("nie", "No definido")
        curso = data.get("curso", "No definido")
        isbn = data.get("isbn", "No definido")
        fecha_entrega = data.get("fecha_entrega", "No definido")
        fecha_devolucion = data.get("fecha_devolucion", "No definido")
        estado = data.get("estado", "P")
        if estado not in ["P", "D"]:
            estado = "P"
        if nie is None or isbn is None:
            raise ValueError("Faltan campos obligatorios (nie o isbn)")
        return Prestamo(nie, curso, isbn, fecha_entrega, fecha_devolucion, estado)

    

    def marcar_como_devuelto(self):
        self.estado = "D"