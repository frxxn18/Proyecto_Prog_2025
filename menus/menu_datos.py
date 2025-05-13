#Carga/Exportación de datos	Cargar datos al inicio, exportar al final 


import os
import pandas as pd
from utils.DataManager import DataManager
from utils.helpers import limpiar_pantalla
from utils.validadores import validar_nie, validar_nombre , validar_isbn
from utils.verificadores import verificar_materias_y_cursos

def cargar_datos():
    print("--Carga de datos--")
    tabla = input("¿Que datos desea cargar? (alumnos,cursos, materias, libros):").strip().lower()

    if tabla == "alumnos":
        nie = input("Ingrese el NIE del alumno:").strip().upper()
        if not validar_nie(nie):
            print("El NIE ingresado no es válido.")
            return
        nombre = input("Ingrese el nombre del alumno:").strip()
        if not validar_nombre(nombre):
            print("El nombre ingresado no es válido.")
        apellidos = input("Ingrese los apellidos:)").strip().title()
        tramo = input("Ingrese el tramo (0,  I, II):").strip().upper()
        bilingue = input("¿El alumno es bilungue? (S/N):").strip().upper() == "S"

        alumno = {
            "nie": nie,
            "nombre": nombre,
            "apellidos": apellidos,
            "tramo": tramo,
            "bilingue": bilingue
        }

        alumnos = DataManager.get_data("alumnos")
        alumnos.append(alumno)
        DataManager.guardar(alumnos, "alumnos")
        print("Alumno agregado con éxito")

    elif tabla == "libros":
        if not verificar_materias_y_cursos():
            return
        isbn = input("Ingrese el ISBN:").strip().replace("-", "")
        if not validar_isbn(isbn):
            print("El ISBN ingresado no es válido.")
            return
        titulo =   input("Ingrese el titulo del libro:").strip() 
        autor = input("Ingrese el autor del libro:").strip()
        ejemplares = int(input("Ingrese el número de ejemplares:").strip())
        id_materia = input("Ingrese el id de la materia:").strip()
        id_curso = input("Ingrese el id del curso:").strip()

        libro = {
            "isbn": isbn,
            "titulo": titulo,
            "autor": autor,
            "numero_ejemplares": ejemplares,
            "id_materia": id_materia,
            "id_curso": id_curso
        }
        
        libros = DataManager.cargar("libros")
        libros.append(libro)
        DataManager.guardar(libros, "libros")
        print("Libro agregado con éxito")
    
    else:
        print("La tabla seleccionada no es válida.")


def guardar_datos():
    print("--Guardar datos--")
    print("Advertencia: (Los datos se guardarán automaticamente despues de cargarlos)")


def exportar_datos():
    print("--Exportar A CSV--")
    tabla = input("¿Que datos desea exportar? (alumnos, libros, etc...:").strip()
    datos = DataManager.cargar(tabla)
    if  not datos:
        print("No hay datos para exportar")
        return
    dataframe = pd.DataFrame(datos)
    dataframe.to_csv(f"{tabla}.csv", index=False)
    print(f"Los datos se han exportado a {tabla}.csv")


def mostrar_menu_datos():
    while True:
        limpiar_pantalla()
        print("--Caga/Exportacion de Datos--")
        print("1. Cargar datos desde los archivos JSON")
        print("2. Guardar datos en los archivos JSON")
        print("3. Exportar datos a CSV")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            cargar_datos()
        elif opcion == "2":
            guardar_datos()
        elif opcion == "3":
            exportar_datos()
        elif opcion == "0":
            break
        else:
            print("Opcion no valida. Pulse ENTER para continuar.")

    

