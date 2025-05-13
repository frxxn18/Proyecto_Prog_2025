#gestor de prestamos

from models.prestamo import Prestamo
from utils.DataManager import DataManager
from utils.verificadores import verificar_fecha

def registrar_prestamo():
    nie = input("NIE del alumno: ").strip().upper()
    curso = input("Curso (ej. 1ESO): ").strip().upper()
    isbn = input("ISBN del libro: ").strip()


    while True:
        fecha_entrega = input("Fecha de entrega (YYYY-MM-DD): ")
        if verificar_fecha(fecha_entrega):
            break
        print("Fecha no válida. Usa el formato YYYY-MM-DD.")

    while True:
        fecha_devolucion = input("Fecha de devolución (YYYY-MM-DD): ")
        if verificar_fecha(fecha_devolucion):
            break
        print("Fecha no válida. Usa el formato YYYY-MM-DD.")

    prestamos = DataManager.cargar("prestamos")
    for prestamo in prestamos:
        if prestamo.nie == nie and prestamo.isbn == isbn and prestamo.estado == "P":
            print("Ya existe un préstamo activo con ese NIE e ISBN.")
            print("Pulsa ENTER para continuar.")
            return
    nuevo = Prestamo(nie, curso, isbn, fecha_entrega, fecha_devolucion)
    prestamos.append(nuevo)
    DataManager.guardar("prestamos", prestamos)
    input("Préstamo registrado correctamente. Pulsa Enter para continuar.")



def ver_prestamos():
    prestamos = DataManager.cargar("prestamos")
    if not prestamos:
        print("No hay préstamos registrados.")
    else:
        for p in prestamos:
            print(p)
    input("\nPulsa Enter para continuar.")


def devolver_libro():
    prestamos = DataManager.cargar("prestamos")
    nie = input("NIE del alumno: ")
    isbn = input("ISBN del libro a devolver: ")

    encontrado = False
    for prestamo in prestamos:
        if prestamo.nie == nie and prestamo.isbn == isbn and prestamo.estado == "P":
            prestamo.marcar_como_devuelto()
            encontrado = True
            break

    if encontrado:
        DataManager.guardar("prestamos", prestamos)
        print("Libro marcado como devuelto.")
    else:
        print("No se encontró un préstamo activo con ese NIE e ISBN.")

    input("Pulsa Enter para continuar.")