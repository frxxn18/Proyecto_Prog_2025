import unittest
from utils.DataManager import DataManager
from models.alumno import Alumno

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

    
    def test_ver_datos_alumno(self):
        alumnos = DataManager.get_data("alumnos")
        self.assertGreater(len(alumnos), 0)
        alumno = alumnos[0]
        self.assertIsNotNone(alumno.nombre)
        self.assertIsNotNone(alumno.apellidos)
        self.assertIsNotNone(alumno.tramo)

    
    def test_filtrar_alumnos(self):
        alumnos = DataManager.get_data("alumnos")
        if not alumnos:
            self.skipTest("No hay alumnos para filtrar")
        nombre = alumnos[0].nombre[3:].lower()
        resultados = [a for a in alumnos if nombre in a.nombre.lower()]
        self.assertGreaterEqual(len(resultados), 1)

    
    def test_añadir_alumno(self):
        alumnos = DataManager.get_data("alumnos")
        nuevo = Alumno("99999999Z", "TestNombre", "TestApellido", "0", False)

        if any(a.nie == nuevo.nie for a in alumnos):
            alumnos = [a for a in alumnos if a.nie != nuevo.nie]
            
        alumnos.append(nuevo)
        DataManager.guardar([a.to_dict() for a in alumnos], "alumnos")

        recargado = DataManager.get_data("alumnos")
        encontrado = any(a.nie == "99999999Z" for a in recargado)
        self.assertTrue(encontrado)

        # Eliminamos el alumno
        recargado = [a for a in recargado if a.nie != "99999999Z"]
        DataManager.guardar([a.to_dict() for a in recargado], "alumnos")

if __name__ == '__main__':
    unittest.main()
