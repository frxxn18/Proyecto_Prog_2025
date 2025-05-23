import unittest
from utils.DataManager import DataManager

class TestAlumnos(unittest.TestCase):

    #comprobacion de la carga de alumnos
    def test_cargar_alumnos(self):
        alumnos = DataManager.get_data("alumnos")
        self.assertIsInstance(alumnos, list)
        for alumno in alumnos:
            self.assertTrue(hasattr(alumno, "nombre"))
            self.assertTrue(hasattr(alumno, "nie"))


    #modificacion del nombre
    def test_modificar_nombre_alumno(self):
        alumnos = DataManager.get_data("alumnos")
        if not alumnos:
            self.skipTest("No hay alumnos para probar")

        alumno = alumnos[0]
        original = alumno.nombre
        alumno.nombre = "NombreDePrueba"

        # Guardamos y recargamos los datos del objeto
        DataManager.guardar([a.to_dict() for a in alumnos], "alumnos")
        recargado = DataManager.get_data("alumnos")[0]
        self.assertEqual(recargado.nombre, "NombreDePrueba")

        # Restauramos los datos del objeto
        recargado.nombre = original
        DataManager.guardar([a.to_dict() for a in alumnos], "alumnos")

if __name__ == '__main__':
    unittest.main()
