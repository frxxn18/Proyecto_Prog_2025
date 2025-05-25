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


    def test_listado_completo_alumnos(self):
        alumnos = DataManager.get_data("alumnos")
        self.assertIsInstance(alumnos, list)
        for alumno in alumnos:
            self.assertTrue(hasattr(alumno, "nie"))
            self.assertTrue(hasattr(alumno, "nombre"))
            self.assertTrue(hasattr(alumno, "apellidos"))

    
    def test_listado_completo_libros(self):
        libros = DataManager.get_data("libros")
        self.assertIsInstance(libros, list)
        for libro in libros:
            self.assertTrue(hasattr(libro, "isbn"))
            self.assertTrue(hasattr(libro, "titulo"))
            self.assertTrue(hasattr(libro, "autor"))

    
    def test_listado_completo_prestamos(self):
        prestamos = DataManager.get_data("prestamos")
        self.assertIsInstance(prestamos, list)
        for p in prestamos:
            self.assertTrue(hasattr(p, "nie"))
            self.assertTrue(hasattr(p, "isbn"))
            self.assertTrue(p.estado in ["P", "D"])




if __name__ == '__main__':
    unittest.main()
