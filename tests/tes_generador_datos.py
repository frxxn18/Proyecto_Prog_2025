import os
import json

# Ruta a la carpeta "data"
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(DATA_DIR, exist_ok=True)

def guardar(tabla, datos):
    path = os.path.join(DATA_DIR, f"{tabla}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    print(f"{tabla} guardado con {len(datos)} registros.")

def generar_datos():
    alumnos = [{
        "nie": "12345678A",
        "nombre": "Juan",
        "apellidos": "Pérez",
        "tramo": "I",
        "bilingüe": True
    }]

    cursos = [{
        "curso": "1ESO",
        "nivel": "Secundaria"
    }]

    materias = [{
        "id": 1,
        "nombre": "Matemáticas",
        "departamento": "Ciencias"
    }]

    libros = [{
        "isbn": "9781234567897",
        "titulo": "Álgebra Básica",
        "autor": "María López",
        "numero_ejemplares": 3,
        "id_materia": 1,
        "id_curso": "1ESO"
    }]

    prestamos = [{
        "nie": "12345678A",
        "curso": "1ESO",
        "isbn": "9781234567897",
        "fecha_entrega": "2024-09-15",
        "fecha_devolucion": "2025-06-20",
        "estado": "P"
    }]

    guardar("alumnos", alumnos)
    guardar("cursos", cursos)
    guardar("materias", materias)
    guardar("libros", libros)
    guardar("prestamos", prestamos)

if __name__ == "__main__":
    generar_datos()
