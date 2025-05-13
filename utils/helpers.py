#aqui iran funciones como limpiar_pantalla o confirmar
import os 
from utils.DataManager import DataManager


def clave_duplicada(lista, clave):
    valores = [item[clave] for item in lista]
    return len(valores) != len(set(valores))

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')