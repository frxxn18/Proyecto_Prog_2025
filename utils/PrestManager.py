#gestor de prestamos

from models.prestamo import Prestamo
from utils.DataManager import DataManager
from utils.verificadores import verificar_fecha
from utils.validadores import validar_nie, validar_isbn
import os

def registrar_prestamo():
    nie = input("NIE del alumno: ").strip().upper()
    curso = input("Curso (ej. 1ESO): ").strip().upper()
    isbn = input("ISBN del libro: ").strip()

#Validacion de los datos
    alumnos = DataManager.cargar("alumnos")
    if not any((a['nie']== nie for a in alumnos)):
        print("El alumno no existe")
        input("Pulsa Enter para continuar")
        return
    
    cursos = DataManager.cargar("cursos")
    if not any((c['curso']== curso for c in cursos)):
        print("El curso no existe")
        input("Pulsa Enter para continuar.")
        return
#Mira si hay stock o no para permitir el prestamo o no
    libros = DataManager.cargar("libros")
    libro = next((l for l in libros if l["isbn"] == isbn), None)
    if not libro:
        print("El libro no existe")
        input("Pulsa Enter para continuar.")
        return
    
    prestamos_cargar = DataManager.cargar("prestamos")
    prestamos = [Prestamo.from_dict(p) for p in prestamos_cargar]
    prestamos_activos = [p for p in prestamos if p.isbn == isbn and p.estado == "P"]
    if len(prestamos_activos) >= libro["numero_ejemplares"]:
        print(f"No hay ejemplares disponibles del libro '{libro['titulo']}' ")
        input("Pulsa Enter para continuar.")
        return

    for prestamo in prestamos:
        if prestamo.nie == nie and prestamo.isbn == isbn and prestamo.estado == "P":
            print("Ya existe un préstamo activo con ese NIE e ISBN.")
            print("Pulsa ENTER para continuar.")
            return


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



    nuevo = Prestamo(nie, curso, isbn, fecha_entrega, fecha_devolucion)
    prestamos.append(nuevo)
    DataManager.guardar([Prestamo.to_dict(p) for p in prestamos], "prestamos")
    input("Préstamo registrado correctamente. Pulsa Enter para continuar.")



def ver_prestamos():
    prestamos_cargar = DataManager.cargar("prestamos")
    prestamos = [Prestamo.from_dict(p) for p in prestamos_cargar]
    if not prestamos:
        print("No hay préstamos registrados.")
    else:
        for p in prestamos:
            print(p)
    input("\nPulsa Enter para continuar.")


def devolver_libro():
    prestamos_cargar = DataManager.cargar("prestamos")
    prestamos = [Prestamo.from_dict(p) for p in prestamos_cargar]
    nie = input("NIE del alumno: ")
    isbn = input("ISBN del libro a devolver: ")

    encontrado = False
    for prestamo in prestamos:
        if prestamo.nie == nie and prestamo.isbn == isbn and prestamo.estado == "P":
            prestamo.marcar_como_devuelto()
            encontrado = True
            break

    if encontrado:
        DataManager.guardar([Prestamo.to_dict(p) for p in prestamos], "prestamos")  
        print("Libro marcado como devuelto.")
    else:
        print("No se encontró un préstamo activo con ese NIE e ISBN.")

    input("Pulsa Enter para continuar.")


def modificar_prestamo():
    prestamos_cargar = DataManager.cargar("prestamos")
    prestamos = [Prestamo.from_dict(p) for p in prestamos_cargar]
    nie = input("NIE del alumno: ").strip().upper()
    if not validar_nie(nie):
        print("NIE no válido")
        input("Pulsa Enter para continuar.")
        return
    
    isbn = input("ISBN del libro: ").strip()
    if not validar_isbn(isbn):
        print("ISBN no válido")
        input("Pulsa Enter para continuar.")
        return

    prestamo = next((p for p in prestamos if p.nie == nie and p.isbn == isbn), None)

    if not prestamo:
        print("No se encontró ningún prestamos con esos datos")
        input("Pulsa Enter para continuar.")
        return
    
    print(f"\nPréstamo encontrado:\n{prestamo}")
    nueva_fecha = input(f"Nueva fecha de devolucion [{prestamo.fecha_devolucion}]:").strip()
    if nueva_fecha:
        from utils.verificadores import verificar_fecha
        if verificar_fecha(nueva_fecha):
            prestamo.fecha_devolucion = nueva_fecha
        else:
            print("La fecha no es valida por lo que se mantendrá la original")


    nuevo_estado = input(f"Nuevo estado (P: Prestado, D: Devuelto) [{prestamo.estado}]: ").strip().upper()
    if nuevo_estado in ["P", "D"]:
        prestamo.estado = nuevo_estado
    
    DataManager.guardar([Prestamo.to_dict(p) for p in prestamos], "prestamos")
    print("Datos actualizados correctamente")
    input("Pulsa Enter para continuar.")



def eliminar_prestamo():
    prestamos_cargar = DataManager.cargar("prestamos")
    prestamos = [Prestamo.from_dict(p) for p in prestamos_cargar]
    nie = input("NIE del alumno: ").strip().upper()
    if not validar_nie(nie):
        print("NIE no válido")
        input("Pulsa Enter para continuar.")
        return
    
    isbn = input("ISBN del libro: ").strip()
    if not validar_isbn(isbn):
        print("ISBN no válido")
        input("Pulsa Enter para continuar.")
        return

    prestamo = next((p for p in prestamos if p.nie == nie and p.isbn == isbn), None)

    if not prestamo:
        print("No se encontró ningún prestamos con esos datos")
        input("Pulsa Enter para continuar.")
        return
    
    print(f"\nPréstamo encontrado:\n{prestamo}")
    print(f" NIE: {prestamo.nie}, ISBN: {prestamo.isbn}, Estado: {prestamo.estado}")
    confirmar = input("¿Seguro desea eliminar este prestamo? (S/N)").strip().upper()
    if confirmar == "S":
        prestamos.remove(prestamo)
        DataManager.guardar([Prestamo.to_dict(p) for p in prestamos], "prestamos")
        print("Préstamo eliminado correctamente")
    else:
        print("Operacion cancelada")
    input("Pulsa Enter para continuar.")



def cerrar_prestamo():
    prestamos_cargar = DataManager.cargar("prestamos")
    prestamos = [Prestamo.from_dict(p) for p in prestamos_cargar]
    nie = input("NIE del alumno: ").strip().upper()
    if not validar_nie(nie):
        print("NIE no válido")
        input("Pulsa Enter para continuar.")
        return
    
    prestamos_alumno = [p for p in prestamos if p.nie == nie]

    if not prestamos_alumno:
        print("Este alumno no tiene prestamos registrados")
    else:
        no_devueltos = [p for p in prestamos_alumno if p.estado != "D"]

        if no_devueltos:
            print("No se puede cerrar el prestamo porque aún hay libros pendientes de devolver")
            for p in no_devueltos:
                print(f" ISBN: {p.isbn}  |  Estado: {p.estado}")
        else:
            print("Todos los libros han sido devueltos, puedes cerrar el prestamo")
    input("Pulsa Enter para continuar.")


def firmar_contrato(nie=None):
    if nie is None:
        nie = input("NIE del alumno: ").strip().upper()
    if not validar_nie(nie):
        print("NIE no válido")
        input("Pulsa Enter para continuar.")
        return
    
    prestamos_cargar = DataManager.cargar("prestamos")
    prestamos = [Prestamo.from_dict(p) for p in prestamos_cargar]
    prestamos_nie = [p for p in prestamos if p.nie == nie]

    if not prestamos_nie:
        print("Este alumno no tiene prestamos registrados")
        input("Pulsa Enter para continuar.")
        return
    
    ruta_base = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))
    ruta_data = os.path.join(ruta_base, "data")
    os.makedirs(ruta_data, exist_ok=True)

    ruta_contrato = os.path.join(ruta_data, f"contrato_{nie}.txt")

    with open(ruta_contrato, "w", encoding="utf-8") as f:
        f.write("CONTRATO DE PRESTAMO DE LIBROS\n")
        f.write(f"NIE del alumno: {nie}\n")
        f.write("Listado de libros: \n\n")
        for p in prestamos_nie:
            estado = "Devuelto" if p.estado == "D" else "Prestado"
            f.write(f"ISBN: {p.isbn}  |  Entrega: {p.fecha_entrega}  |  Devolución:  {p.fecha_devolucion}  |  Estado: {estado}\n")
        
        f.write("\nFirma del alumno: ______________\n")
        f.write("Firma del centro: ______________\n")
    
    print(f"Contrato guardado en {ruta_contrato}")
    input("Pulsa Enter para continuar.")



def cambiar_curso_alumno():
    nie = input("Introduzca el NIE del alumno:").strip().upper()
    nuevo_curso = input("Introduzca el nuevo curso:").strip().upper()
    if not validar_nie(nie):
        print("NIE no válido")
        input("Pulsa Enter para continuar.")
        return
    
    prestamos_dict = DataManager.cargar("prestamos")
    prestamos = [Prestamo.from_dict(p) for p in prestamos_dict]
    encontrados = 0

    for prestamo in prestamos:
        if prestamo.nie == nie:
            prestamo.curso = nuevo_curso
            encontrados += 1

    if encontrados == 0:
        print("No se encontraron prestamos para el alumno.")
        input("Pulsa Enter para continuar.")
        return

    DataManager.guardar([p.to_dict() for p in prestamos], "prestamos")
    print(f"{encontrados} prestamos modificados al curso {nuevo_curso} para el nie {nie}")
    input("Pulsa Enter para continuar.")