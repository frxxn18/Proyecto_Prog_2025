#Generación de listados	Mostrar libros por curso, estado, etc.

from utils.helpers import limpiar_pantalla
from utils.DataManager import DataManager

def listado_alumnos():
    alumnos = DataManager.cargar("alumnos")
    if not alumnos:
        print("No hay alumnos registrados")
    else:
        for a in alumnos:
            bilingüe = "Sí" if a["bilingüe"] else "No"
            print(f"NIE: {a['nie']} | Nombre: {a['nombre']} | Apellidos: {a['apellidos']} | Tramo: {a['tramo']} | Bilingüe: {bilingüe}")
    input("Pulsa Enter para continuar.")


def listado_libros():
    libros = DataManager.cargar("libros")
    if not libros:
        print("No hay libros registrados")
    else:
        for l in libros:
            print(f"ISBN: {l['isbn']} | Título: {l['titulo']} | Autor: {l['autor']}")
    input("Pulsa Enter para continuar.")


def listado_prestamos():
    prestamos = DataManager.cargar("prestamos")
    if not prestamos:
        print("No hay préstamos registrados")
    else:
        for p in prestamos:
            estado = "Devuelto" if p["estado"] == "D" else "Prestado"
            print(f"NIE: {p['nie']} | ISBN: {p['isbn']} | Entrega: {p['fecha_entrega']} | Devolución:  {p['fecha_devolucion']} | Estado: {estado} | Curso: {p['curso']}")
    input("Pulsa Enter para continuar.")


def mostrar_menu_listados():
    while True:
        limpiar_pantalla()
        print("=== MENÚ DE LISTADOS ===")
        print("1. Listado de alumnos")
        print("2. Listado de libros")
        print("3. Listado de préstamos")
        print("0. Volver al menú principal")
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "1":
            listado_alumnos()
        elif opcion == "2":
            listado_libros()
        elif opcion == "3":
            listado_prestamos()
        elif opcion == "0":
            break
        else:
            input("Opción no válida. Pulsa ENTER para continuar.")