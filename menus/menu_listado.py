#Generación de listados	Mostrar libros por curso, estado, etc.


import os

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_listados():
    while True:
        limpiar()
        print("=== LISTADOS ===")
        print("1. Listado de libros por curso")
        print("2. Listado de alumnos con préstamos")
        print("3. Listado de préstamos activos")
        print("0. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
           """listado de libros por curso"""
        elif opcion == "2":
            """listado de alumnos con prestamos"""
        elif opcion == "3":
            """listado de prestamos activos"""
        elif opcion == "0":
            break
        else:
            input("Opción no válida. Pulsa ENTER para continuar.")



