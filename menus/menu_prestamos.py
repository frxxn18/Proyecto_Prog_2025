#Gestión de préstamos	Asignar, devolver, cerrar préstamo



import os

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_prestamos():
    while True:
        limpiar()
        print("=== GESTIÓN DE PRÉSTAMOS ===")
        print("1. Asignar préstamo")
        print("2. Devolver libro")
        print("3. Ver préstamos por alumno")
        print("0. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            """asignar_prestamo()"""
        elif opcion == "2":
            """devolver_libro()"""
        elif opcion == "3":
            """mostrar_prestamos()"""
        elif opcion == "0":
            break
        else:
            input("Opción no válida. Pulsa ENTER para continuar.")
