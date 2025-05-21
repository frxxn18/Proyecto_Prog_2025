from utils.helpers import limpiar_pantalla
from utils.PrestManager import (
    registrar_prestamo,
    ver_prestamos,
    devolver_libro,
    modificar_prestamo,
    eliminar_prestamo,
    cerrar_prestamo,
    firmar_contrato,
    cambiar_curso_alumno
)

def mostrar_menu_prestamos():
    while True:
        limpiar_pantalla()
        print("=== MENÚ DE PRÉSTAMOS ===")
        print("1. Registrar préstamo")
        print("2. Ver préstamos")
        print("3. Devolver libro")
        print("4. Modificar préstamo (Submenu)")
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
            mostrar_submenu_modificacion()
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



def mostrar_submenu_modificacion():
    while True:
        limpiar_pantalla()
        print("--Menu de modificación--")
        print("1. Cambiar curso alumno")
        print("2. Modificar estado y fecha")
        print("0. Volver")

        subopcion = input("Selecciona una opción: ").strip()
        if subopcion == "1":
            cambiar_curso_alumno()
        elif subopcion == "2":
            modificar_prestamo()
        elif subopcion == "0":
            break
        else:
            input("Opción no válida. Pulsa ENTER para continuar.")