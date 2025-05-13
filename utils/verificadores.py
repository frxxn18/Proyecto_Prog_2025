from utils import DataManager

def verificar_materias_y_cursos():
    materias = DataManager.cargar("materias")
    cursos = DataManager.cargar("cursos")
    if not materias or not cursos:
        print("Antes de cargar libros, debe haber materias y cursos")
        return False
    return True