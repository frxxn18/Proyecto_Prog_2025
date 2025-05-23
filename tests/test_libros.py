import unittest
from utils.DataManager import DataManager
from models.libro import Libro

class TestLibros(unittest.TestCase):

    def test_cargar_libros(self):
        libros = DataManager.get_data("libros")
        self.assertIsInstance(libros, list)
        for libro in libros:
            self.assertIsInstance(libro, Libro)
            self.assertTrue(hasattr(libro, "isbn"))
            self.assertTrue(hasattr(libro, "titulo"))

    def test_modificar_titulo_libro(self):
        libros = DataManager.get_data("libros")
        if not libros:
            self.skipTest("No hay libros para probar")

        libro = libros[0]
        original = libro.titulo
        libro.titulo = "Título de Prueba"

        # Guardar con cambio
        DataManager.guardar([l.to_dict() for l in libros], "libros")

        # Recargar y comprobar los datos
        recargado = DataManager.get_data("libros")[0]
        self.assertEqual(recargado.titulo, "Título de Prueba")

        # Restaurar título original
        recargado.titulo = original
        DataManager.guardar([l.to_dict() for l in libros], "libros")

if __name__ == '__main__':
    unittest.main()
