#	Gestión de libros	Añadir libros, ver inventario

from utils.helpers import limpiar_pantalla
from utils.DataManager import DataManager
from utils.validadores import validar_isbn

def ver_libros():
    libros = DataManager.cargar("libros")
    if not libros:
        print("No hay libros registrados")
    else:
        for libro in libros:
            print(f"ISBN: {libro['isbn']} | Título: {libro['titulo']} | Autor: {libro['autor']}")
    input("Pulsa Enter para continuar.")


def eliminar_libro():
    libros = DataManager.cargar("libros")
    isbn = input("ISBN del libro a eliminar: ").strip()
    if not validar_isbn(isbn):
        print("ISBN no válido")
        input("Pulsa Enter para continuar.")
        return
    
    libro = next((l for l in libros if l["isbn"] == isbn), None)
    if not libro:
        print("No se encontró ningun libro con ese ISBN")
    else:
        confirmar = input(f"¿Seguro desea eliminar el libro {libro['titulo']}? (S/N)").strip().upper()
        if confirmar == "S":
            libros.remove(libro)
            DataManager.guardar(libros, "libros")
            print("Libro eliminado correctamente")
        else:
            print("Operación cancelada")
    input("Pulsa Enter para continuar.")


def filtrar_libros():
    filtro = input("Ingrese parte del título o ISBN:").strip().lower()
    libros = DataManager.cargar("libros")
    resultados = [l for l in libros if filtro in l["titulo"].lower() or filtro in l["isbn"] or filtro in l["autor"].lower()]
    if not resultados:
        print("No hay libros que coincidan con el filtro")
    else:
        for libro in resultados:
            print(f"ISBN: {libro['isbn']} | Título: {libro['titulo']} | Autor: {libro['autor']}")
    input("Pulsa Enter para continuar.")


def modificar_libro():
    libros = DataManager.cargar("libros")
    isbn = input("Introduce el ISBN del libro a modificar: ").strip()
    if not validar_isbn(isbn):
        print("ISBN no válido.")
        input("Pulsa ENTER para continuar.")
        return
    libro = next((l for l in libros if l["isbn"] == isbn), None)
    if not libro:
        print("No se encontró ningún libro con ese ISBN.")
    else:
        print("Introduce los nuevos datos (deja en blanco para mantener el actual):")
        nuevo_titulo = input(f"Título [{libro['titulo']}]: ").strip() or libro['titulo']
        nuevo_autor = input(f"Autor [{libro['autor']}]: ").strip() or libro['autor']
        nuevo_ejemplares = input(f"Número de ejemplares [{libro['numero_ejemplares']}]: ").strip()
        nuevo_id_materia = input(f"ID Materia [{libro['id_materia']}]: ").strip() or libro['id_materia']
        nuevo_id_curso = input(f"ID Curso [{libro['id_curso']}]: ").strip() or libro['id_curso']

        libro['titulo'] = nuevo_titulo
        libro['autor'] = nuevo_autor
        if nuevo_ejemplares.isdigit():
            libro['numero_ejemplares'] = int(nuevo_ejemplares)
        libro['id_materia'] = nuevo_id_materia
        libro['id_curso'] = nuevo_id_curso

        DataManager.guardar(libros, "libros")
        print("Libro modificado correctamente.")
    input("Pulsa ENTER para continuar.")



def mostrar_menu_libros():
    while True:
        limpiar_pantalla()
        print("=== MENÚ DE LIBROS ===")
        print("1. Ver libros")
        print("2. Eliminar libro")
        print("3. Filtrar libros")
        print("0. Volver al menú principal")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            ver_libros()
        elif opcion == "2":
            eliminar_libro()
        elif opcion == "3":
            modificar_libro()
        elif opcion == "4":
            filtrar_libros()
        elif opcion == "0":
            break
        else:
            input("Opción no válida. Pulsa ENTER para continuar.")
