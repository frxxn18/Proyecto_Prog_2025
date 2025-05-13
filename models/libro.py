class Libro:
    def __init__(self, isbn: str, titulo: str, autor: str, numero_ejemplares: int, id_materia: int, id_curso: str):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.numero_ejemplares = numero_ejemplares
        self.id_materia = id_materia
        self.id_curso = id_curso

    def __str__(self):
        return (
            f"ISBN: {self.isbn}, Título: {self.titulo}, Autor: {self.autor}, "
            f"Ejemplares: {self.numero_ejemplares}, Materia ID: {self.id_materia}, Curso ID: {self.id_curso}"
        )

    def to_dict(self):
        return {
            "isbn": self.isbn,
            "titulo": self.titulo,
            "autor": self.autor,
            "numero_ejemplares": self.numero_ejemplares,
            "id_materia": self.id_materia,
            "id_curso": self.id_curso
        }

    @staticmethod
    def from_dict(data: dict):
        return Libro(
            isbn=data["isbn"],
            titulo=data["titulo"],
            autor=data["autor"],
            numero_ejemplares=data["numero_ejemplares"],
            id_materia=data["id_materia"],
            id_curso=data["id_curso"]
        )
