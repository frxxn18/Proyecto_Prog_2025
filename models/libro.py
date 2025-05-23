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
        isbn = data.get("isbn", "No definido")
        titulo = data.get("titulo", "No definido")
        autor = data.get("autor", "No definido")
        numero_ejemplares = data.get("numero_ejemplares", 1)
        id_materia = data.get("id_materia", 0)
        id_curso = data.get("id_curso", "No definido")

        if isbn is None:
            raise ValueError("Falta campo obligatorio")
        if titulo is None:
            print(f"Libro {isbn} no tiene titulo, se le asignara --> No definido ")
        if autor is None:
            print(f"Libro {isbn} no tiene autor, se le asignara --> No definido ")
        
        return Libro(
            isbn = isbn,
            titulo = titulo,
            autor = autor,
            numero_ejemplares = numero_ejemplares,
            id_materia = id_materia,
            id_curso = id_curso
        )
