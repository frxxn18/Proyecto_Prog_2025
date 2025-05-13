from utils import DataManager
from datetime import datetime

def verificar_materias_y_cursos():
    materias = DataManager.cargar("materias")
    cursos = DataManager.cargar("cursos")
    if not materias or not cursos:
        print("Antes de cargar libros, debe haber materias y cursos")
        return False
    return True



def verificar_fecha(fecha_str: str) -> bool:
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False