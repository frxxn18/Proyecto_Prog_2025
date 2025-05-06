#Carga/Exportación de datos	Cargar datos al inicio, exportar al final 


import os

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_datos():
    while True:
        limpiar()
        print("=== CARGA / EXPORTACIÓN DE DATOS ===")
        print("1. Cargar datos desde JSON")
        print("2. Guardar datos a JSON")
        print("3. Exportar datos a CSV")
        print("0. Volver al menú principal")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            """cargar_datos()"""
        elif opcion == "2":
            """guardar_datos()"""
        elif opcion == "3":
            """exportar_datos()"""
        elif opcion == "0":
            break
        else:
            input("Opción no válida. Pulsa ENTER para continuar.")




