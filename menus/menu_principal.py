#	Menú principal	Entrada a todos los submenús

import os
from menus import menu_alumnos, menu_libros, menu_prestamos, menu_listados, menu_datos
from utils.helpers import limpiar_pantalla

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_principal():
    while True:
        limpiar_pantalla()
        print("=== MENÚ PRINCIPAL ===")
        print("1. Gestión de Alumnos")
        print("2. Gestión de Libros")
        print("3. Gestión de Préstamos")
        print("4. Listados")
        print("5. Cargar / Exportar datos")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            menu_alumnos.mostrar_menu_alumnos()
        elif opcion == "2":
            menu_libros.mostrar_menu_libros()
        elif opcion == "3":
            menu_prestamos.mostrar_menu_prestamos()
        elif opcion == "4":
            menu_listados.mostrar_menu_listados()
        elif opcion == "5":
            menu_datos.mostrar_menu_datos()
        elif opcion == "0":
            print("Saliendo del sistema.")
            break
        else:
            input("Opción no válida. Pulsa ENTER para continuar.")
