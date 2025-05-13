#Gestión de alumnos	Añadir, modificar, ver datos de alumnos 
from utils.DataManager import DataManager
from utils.helpers import limpiar_pantalla
from utils.validadores import validar_nombre, validar_nie

def ver_datos_alumno():
    nie = input("Introduzca el NIE del alumno:").strip().lower()
    if not validar_nie(nie):
        print("NIE no válido")


    alumnos = DataManager.cargar("alumnos")
    alumno = next((a for a in alumnos if a ["nie"] == nie), None)

    if not alumno:
        print("No existe alumno con ese NIE")
        return
    
    print(f"\nDatos del alumno {nie}:")
    print(f"- Nombre: {alumno['nombre']}")
    print(f"- Apellidos: {alumno['apellidos']}")
    print(f"- Tramo: {alumno['tramo']}")
    print(f"- Bilingüe: {'Sí' if alumno['bilingüe'] else 'No'}")


    #Mostrar los prestamos asociados
    prestamos = DataManager.cargar("prestamos")
    asociados = [p for p in prestamos if p["nie"] == nie]
    if asociados:
        print("- Prestamos")
        for p in asociados:
            estado = "Devuelto" if p["estado"] == "D" else "Prestado"
            print(f"  * ISBN: {p['isbn']}  |  Entrega: {p['fecha_entrega']}  |  Devolución:  {p['fecha_devolucion']}  |  Estado: {estado}")
    else:
        print("- No hay prestamos asociados")


def modificar_alumno():
    nie = input("Introduzca el NIE del alumno:").strip().lower()
    if not validar_nie(nie):
        print("NIE no válido")
        return
    
    alumnos = DataManager.cargar("alumnos")
    index = next((i for i, a in enumerate(alumnos) if a["nie"] == nie), None)

    if index is None:
        print("No existe alumno con ese NIE")
        return
    
    alumno = alumnos[index]
    ver_datos_alumno()
    confirmacion = input("¿Desea modificar los datos? (S/N)").strip().upper()
    if confirmacion != "S":
        print("Datos no modificados")
        return
    
    nuevo_nombre = input(f"Nuevo nombre [{alumno['nombre']}]: ") or alumno['nombre']
    if not validar_nombre(nuevo_nombre):
        print("Nombre no válido")
        return
    
    nuevos_apellidos = input(f"Nuevos apellidos [{alumno['apellidos']}]: ") or alumno['apellidos']
    nuevo_tramo = input(f"Nuevo tramo [{alumno['tramo']}]: ") or alumno['tramo']
    nuevo_bilingüe = input(f"¿Es bilingüe? (S/N) [{ 'S' if alumno['bilingüe'] else 'N' }]: ") or ('S' if alumno['bilingüe'] else 'N')

    alumnos[index] = {
        "nie": nie,
        "nombre": nuevo_nombre,
        "apellidos": nuevos_apellidos,
        "tramo": nuevo_tramo,
        "bilingüe": nuevo_bilingüe.upper() == "S"
    }

    DataManager.guardar(alumnos, "alumnos")
    print("Datos actualizados correctamente")



def filtrar_alumnos():
    filtro = input("Introduzca parte del nombre, NIE o apellidos:").strip().lower()
    alumnos = DataManager.cargar("alumnos")
    resultados = [a for a in alumnos if filtro in a["nie"].lower() or filtro in a["nombre"].lower() or filtro in a["apellidos"].lower()]

    if not resultados:
        print("No hay alumnos que coincidan con el filtro")
    else:
        for alumno in resultados:
            bilingüe = "S" if alumno["bilingüe"] else "N"
            print(f"NIE: {alumno['nie']} | Nombre: {alumno['nombre']} | Apellidos: {alumno['apellidos']} | Tramo: {alumno['tramo']} | Bilingüe: {bilingüe}")



def mostrar_menu_alumnos():
    while True:
        limpiar_pantalla()
        print("--Gestion de alumnos--")
        print("1. Ver datos de alumnos")
        print("2. Modificar datos de un alumno")
        print("3. Filtrar alumnos")
        print("0. Volver al menu principal")

        opcion = input("Seleccione una opción del menú:")
        if opcion == "1":
            ver_datos_alumno()
        elif opcion == "2":
            modificar_alumno()
        elif opcion == "3":
            filtrar_alumnos()
        elif opcion == "0":
            break
        else:
            print("Opción incorrecta")