#Carga/Exportación de datos	Cargar datos al inicio, exportar al final 

import json
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
        bilingüe = input("¿El alumno es bilungue? (S/N):").strip().upper() == "S"

        alumno = {
            "nie": nie,
            "nombre": nombre,
            "apellidos": apellidos,
            "tramo": tramo,
            "bilingüe": bilingüe
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
    tablas = ["alumnos", "cursos", "materias", "libros", "prestamos"]
    for tabla in tablas:
        en_archivo = DataManager.cargar(tabla)
        en_memoria =DataManager.cargar(tabla)

        fusionado = en_archivo.copy()
        añadidos = 0

        if tabla == "prestamos":
            claves_existentes = set((p['nie'], p['isbn'], p['curso']) for p in en_memoria)
            for nuevo in en_memoria:
                clave = (nuevo['nie'], nuevo['isbn'], nuevo['curso'])
                if clave not in claves_existentes:
                    fusionado.append(nuevo)
                    claves_existentes.add(clave)
                    añadidos += 1
        else:
            if tabla == "cursos":
                clave = "curso"
            elif tabla == "materias":
                clave = "id"
            elif tabla == "alumnos":
                clave = "nie"
            elif tabla == "libros":
                clave = "isbn"
            else:
                clave = "id"
            claves_existentes = set(p[clave] for p in fusionado)
            for nuevo in en_memoria:
                if nuevo[clave] not in claves_existentes:
                    fusionado.append(nuevo)
                    claves_existentes.add(nuevo[clave])
                    añadidos += 1
            DataManager.guardar(fusionado, tabla)
            print(f"Se añadieron {añadidos} nuevos elementos a {tabla}")
    input("Pulsa ENTER para continuar.")


def exportar_datos_a_elegir():
    print("--Exportar datos a eleccion--")
    tabla = input("¿Que datos desea exportar? (alumnos, libros, prestamos):").strip().lower()
    formato =input("¿En qué formato desea exportar? (csv, json):").strip().lower()

    datos = DataManager.cargar(tabla)
    if  not datos:
        print("No hay datos para exportar")
        return
    
    if formato == "csv":
        pd.DataFrame(datos).to_csv(f"{tabla}.csv", index=False)
    elif formato == "json":
        with open(f"{tabla}.json", "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)
    else:
        print("Formato de exportación no válido")
    print(f"Datos exportados con éxito a {tabla}.{formato}")


def exportar_todo_en_formato():
    print("--Exportar todos los  datos--")
    formato = input("¿En qué formato desea exportar? (csv, json):").strip().lower()
    tablas = ["alumnos", "cursos", "materias", "libros", "prestamos"]

    for tabla in tablas:
        datos = DataManager.cargar(tabla)
        if not datos:
            continue
            
        if formato == "csv":
            pd.DataFrame(datos).to_csv(f"{tabla}.csv", index=False)
        elif formato == "json":
            with open(f"{tabla}.json", "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
        else:
            print("Formato de exportación no válido")
        print(f"Datos exportados con éxito a {tabla}.{formato}")



def vaciar_datos():
    print("-- Vaciar todos los datos del sistema --")
    confirmacion = input("¿Estás seguro de que deseas vaciar TODOS los datos? (S/N): ").strip().upper()
    if confirmacion == "S":
        rutas = ["alumnos", "cursos", "materias", "libros", "prestamos"]
        DataManager.vaciar_base(rutas)
        print("Todos los archivos han sido vaciados correctamente.")
    else:
        print("Operación cancelada.")
    input("Pulsa ENTER para continuar.")



def crear_backup():
    print("--Creacion de backup--")
    carpeta_backup = "backup"
    os.makedirs(carpeta_backup, exist_ok=True)

    tablas = ["alumnos", "cursos", "materias", "libros", "prestamos"]
    for tabla in tablas:
        datos = DataManager.cargar(tabla)
        if datos:
            ruta_backup = os.path.join(carpeta_backup, f"{tabla}_back.json")
            with open(ruta_backup, "w", encoding="utf-8") as f:
                json.dump(datos, f, indent=4, ensure_ascii=False)
                print(f"Datos de {tabla} guardados con éxito en {ruta_backup}")
        else:
            print(f"No hay datos de {tabla} para guardar, no se genera backup")
    print("Backup creado con éxito")










def mostrar_menu_datos():
    while True:
        limpiar_pantalla()
        print("--Caga/Exportacion de Datos--")
        print("1. Cargar datos desde los archivos JSON")
        print("2. Guardar estado actual en los archivos JSON")
        print("3. Exportar datos a eleccion")
        print("4. Exportar todos los datos")
        print("5. Vaciar los datos")
        print("6. Crear backup")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            cargar_datos()
        elif opcion == "2":
            guardar_datos()
        elif opcion == "3":
            exportar_datos_a_elegir()
        elif opcion == "4":
            exportar_todo_en_formato()
        elif opcion == "5":
            vaciar_datos()
        elif opcion == "6":
            crear_backup()
        elif opcion == "0":
            break
        else:
            print("Opcion no valida. Pulse ENTER para continuar.")

    

