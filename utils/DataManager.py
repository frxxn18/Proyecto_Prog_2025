import os 
import json
from models.alumno import Alumno
from models.libro import Libro
from models.materia import Materia
from models.curso import Curso
from models.prestamo import Prestamo
from utils.validadores import validar_nie, validar_isbn


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
MEMORIA = {}
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
        if tabla in MEMORIA:
            return MEMORIA[tabla]
        
        datos = DataManager.cargar(tabla)
        if tabla == "alumnos":
            objetos = []
            nies_existentes = set()
            for d in datos:
                try:
                    if not validar_nie(d["nie"]):
                        print(f"NIE no válido: {d['nie']}")
                        continue
                    if d["nie"] in nies_existentes:
                        print(f"NIE duplicado: {d['nie']}")
                        continue
                    alumno = Alumno.from_dict(d)
                    objetos.append(alumno)
                    nies_existentes.add(d["nie"])
                except Exception as e:
                    print(f"Error al cargar alumno {d['nie']}: {e}")
        elif tabla == "cursos":
            objetos = [Curso.from_dict(d) for d in datos]
        elif tabla == "materias":
            objetos = [Materia.from_dict(d) for d in datos]
        elif tabla == "libros":
            objetos = []
            isbns = set()
            for d in datos:
                try:
                    if not validar_isbn(d["isbn"]):
                        print(f"ISBN no válido: {d['isbn']}")
                        continue
                    if d["isbn"] in isbns:
                        print(f"ISBN duplicado: {d['isbn']}")
                        continue
                    libro = Libro.from_dict(d)
                    objetos.append(libro)
                    isbns.add(d["isbn"])
                except Exception as e:
                    print(f"Error al cargar libro {d['isbn']}: {e}")
        elif tabla == "prestamos":
            objetos = []
            claves_prestamos = set()
            for d in datos:
                try:
                    clave = (d['nie'], d['isbn'], d['curso'])
                    if clave in claves_prestamos:
                        print(f"Préstamo duplicado: {clave[0]} ISBN:{clave[2]}")
                        continue
                    prestamo = Prestamo.from_dict(d)
                    objetos.append(prestamo)
                    claves_prestamos.add(clave)
                except Exception as e:
                    print(f"Error al cargar préstamo {clave}: {e}")
        else:
            objetos = datos
        MEMORIA[tabla] = objetos
        return objetos