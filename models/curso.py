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
        curso = data.get("curso", "No definido")
        nivel = data.get("nivel", "No definido")

        if curso is None:
            raise ValueError("Falta campo obligatorio")
        if nivel is None:
            print(f"Curso {curso} no tiene nivel, se le asignara --> No definido ")

        return Curso(
            curso = curso,
            nivel = nivel
        )