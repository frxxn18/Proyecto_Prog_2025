class Curso:
    def __init__(self, curso: str, nivel: str):
        self.curso = curso
        self.nivel = nivel

    def __str__(self):
        return f"Curso: {self.curso}, Nivel: {self.nivel}"

    def to_dict(self):
        return {
            "curso": self.curso,
            "nivel": self.nivel
        }

    @staticmethod
    def from_dict(data: dict):
        return Curso(
            curso=data["curso"],
            nivel=data["nivel"]
        )