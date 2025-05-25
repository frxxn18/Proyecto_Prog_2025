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


    def test_filtrar_libros(self):
        libros = DataManager.get_data("libros")
        if not libros:
            self.skipTest("No hay libros disponibles para filtrar")
        fragmento = libros[0].titulo[:3].lower()
        filtrados = [l for l in libros if fragmento in l.titulo.lower()]
        self.assertGreaterEqual(len(filtrados), 1)


    def test_eliminar_libro_temporal(self):
        libros = DataManager.get_data("libros")
        nuevo = Libro("9999999999999", "TempLibro", "TempAutor", 1, 1, "1ESO")
        libros.append(nuevo)
        DataManager.guardar([l.to_dict() for l in libros], "libros")

        libros_actualizados = DataManager.get_data("libros")
        self.assertTrue(any(l.isbn == "9999999999999" for l in libros_actualizados))

        # eliminarlo
        libros_limpios = [l for l in libros_actualizados if l.isbn != "9999999999999"]
        DataManager.guardar([l.to_dict() for l in libros_limpios], "libros")





if __name__ == '__main__':
    unittest.main()
