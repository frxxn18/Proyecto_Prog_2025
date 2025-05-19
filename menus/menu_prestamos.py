from utils.helpers import limpiar_pantalla
from utils.PrestManager import (
    registrar_prestamo,
    ver_prestamos,
    devolver_libro,
    modificar_prestamo,
    eliminar_prestamo,
    cerrar_prestamo,
    firmar_contrato
)

def mostrar_menu_prestamos():
    while True:
        limpiar_pantalla()
        print("=== MENÚ DE PRÉSTAMOS ===")
        print("1. Registrar préstamo")
        print("2. Ver préstamos")
        print("3. Devolver libro")
        print("4. Modificar préstamo")
        print("5. Eliminar préstamo")
        print("6. Cerrar préstamo")
        print("7. Firmar contrato")
        print("0. Volver al menú principal")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            registrar_prestamo()
        elif opcion == "2":
            ver_prestamos()
        elif opcion == "3":
            devolver_libro()
        elif opcion == "4":
            modificar_prestamo()
        elif opcion == "5":
            eliminar_prestamo()
        elif opcion == "6":
            cerrar_prestamo()
        elif opcion == "7":
            firmar_contrato()
        elif opcion == "0":
            break
        else:
            input("Opción no válida. Pulsa ENTER para continuar.")