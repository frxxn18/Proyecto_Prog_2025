import os 
import json
from models.alumno import Alumno
from models.libro import Libro
from models.materia import Materia
from models.curso import Curso
from models.prestamo import Prestamo

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

class DataManager:


    @staticmethod
    def pasar_json(objetos):
        if isinstance(objetos, dict):
            serializable = {}
            for key, value in objetos.items():
                clave = str(key)
                if hasattr(value, 'to_dict'):
                    valor = value.to_dict()
                else:
                    valor = value
                serializable[clave] = valor
            return json.dumps(serializable, indent=4)
        
        elif isinstance(objetos, list):
            serializable = []
            for item in objetos:
                if hasattr(item, 'to_dict'):
                    serializable.append(item.to_dict())
                else:
                    serializable.append(item)
            return json.dumps(serializable, indent=4)

        else:
            return json.dumps(objetos, indent=4)



    @staticmethod
    def guardar(diccionario, ruta):
        composed_path = os.path.join(DATA_DIR, ruta + ".json")
        os.makedirs(os.path.dirname(composed_path), exist_ok=True)
        with open(composed_path, 'w', encoding='utf-8') as f:
            f.write(DataManager.pasar_json(diccionario))
        print("Datos guardados en el archivo", ruta)
        input("Presiona Enter para continuar... \n")


    @staticmethod
    def cargar(ruta):
        composed_path = os.path.join(DATA_DIR, ruta + ".json")
        datos = {}
        if os.path.exists(composed_path):
            with open(composed_path, 'r', encoding='utf-8') as f:
                datos = json.loads(f.read())
        return datos


    @staticmethod
    def vaciar_base(rutas: list):
        for ruta in rutas:
            DataManager.guardar([], ruta)


    @staticmethod
    def get_data(tabla):
        datos = DataManager.cargar(tabla)
        if tabla == "alumnos":
            return [Alumno.from_dict(d) for d in datos]
        elif tabla == "cursos":
            return [Curso.from_dict(d) for d in datos]
        elif tabla == "materias":
            return [Materia.from_dict(d) for d in datos]
        elif tabla == "libros":
            return [Libro.from_dict(d) for d in datos]
        elif tabla == "prestamos":
            return [Prestamo.from_dict(d) for d in datos]