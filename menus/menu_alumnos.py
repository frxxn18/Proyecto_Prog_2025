#Gestión de alumnos	Añadir, modificar, ver datos de alumnos 


import os

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_alumnos():
    while True:
        limpiar()
        print("=== GESTIÓN DE ALUMNOS ===")
        print("1. Ver todos los alumnos")
        print("2. Añadir alumno")
        print("3. Modificar alumno")
        print("4. Eliminar alumno")
        print("0. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            """mostrar_listado_alumnos()"""
        elif opcion == "2":
            """añadir_alumno()"""
        elif opcion == "3":
            """modificar_alumno()"""
        elif opcion == "4":
            """eliminar_alumno()"""
        elif opcion == "0":
            break
        else:
            input("Opción no válida. Pulsa ENTER para continuar.")
