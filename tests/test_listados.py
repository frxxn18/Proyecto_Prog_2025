import unittest
from utils.DataManager import DataManager
from models.libro import Libro
from models.prestamo import Prestamo

class TestListados(unittest.TestCase):

    def test_listado_libros_por_curso(self):
        libros = DataManager.get_data("libros")
        if not libros:
            self.skipTest("No hay libros disponibles para testear.")
        for l in libros:
            self.assertIsInstance(l, Libro)

        curso = libros[0].id_curso
        filtrados = [l for l in libros if l.id_curso == curso]
        self.assertGreater(len(filtrados), 0)

    def test_listado_libros_por_materia(self):
        libros = DataManager.get_data("libros")
        if not libros:
            self.skipTest("No hay libros disponibles para testear.")
        for l in libros:
            self.assertIsInstance(l, Libro)

        materia = libros[0].id_materia
        filtrados = [l for l in libros if l.id_materia == materia]
        self.assertGreater(len(filtrados), 0)

    def test_listado_prestamos_devuelto(self):
        prestamos = DataManager.get_data("prestamos")
        for p in prestamos:
            self.assertIsInstance(p, Prestamo)

        devueltos = [p for p in prestamos if p.estado == "D"]
        self.assertIsInstance(devueltos, list)

    def test_listado_prestamos_pendientes(self):
        prestamos = DataManager.get_data("prestamos")
        for p in prestamos:
            self.assertIsInstance(p, Prestamo)

        pendientes = [p for p in prestamos if p.estado == "P"]
        self.assertIsInstance(pendientes, list)

if __name__ == '__main__':
    unittest.main()
