#Carga/Exportación de datos	Cargar datos al inicio, exportar al final 

import json
import os
import pandas as pd
from utils.DataManager import DataManager
from utils.helpers import limpiar_pantalla


def cargar_datos():
    print("--Carga de datos--")

    tablas = ["alumnos", "cursos", "materias", "libros", "prestamos"]
    for tabla in tablas:
        try:
            datos = DataManager.get_data(tabla)
            print(f"Se cargaron {len(datos)} elementos de {tabla}")
        except Exception as e:
            print(f"No se pudo cargar {tabla} porque: {e}")
    
    input("Pulsa ENTER para continuar.")



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

    

