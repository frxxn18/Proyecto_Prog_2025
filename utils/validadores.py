#aqui ira la funcion para validar cualquier tipo de cosa

import re

def validar_nie(nie):
    return re.fullmatch(r"^[0-9]{8}[A-Z]$", nie) is not None

def validar_nombre(nombre):
    return re.fullmatch(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$", nombre) is not None

def validar_isbn(isbn):
    return re.fullmatch(r"^(97(8|9))?\d{9}(\d|X)$", isbn) is not None

def validar_departamento(departamento):
    return re.fullmatch(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ ]+$", departamento) is not None
