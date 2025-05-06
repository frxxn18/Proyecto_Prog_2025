#	Gestión de libros	Añadir libros, ver inventario


import os

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_libros():
    while True:
        limpiar()
        print("=== GESTIÓN DE LIBROS ===")
        print("1. Ver inventario")
        print("2. Añadir libro")
        print("3. Modificar libro")
        print("0. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            """mostrar_listado_libros()"""
        elif opcion == "2":
            """añadir_libro()"""
        elif opcion == "3":
            """modificar_libro()"""
        elif opcion == "0":
            break
        else:
            input("Opción no válida. Pulsa ENTER para continuar.")
