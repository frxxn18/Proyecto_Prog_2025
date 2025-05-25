import unittest
from utils.DataManager import DataManager
from models.prestamo import Prestamo
import os 
from utils.PrestManager import firmar_contrato

class TestPrestamos(unittest.TestCase):

    def test_cargar_prestamos(self):
        prestamos = DataManager.get_data("prestamos")
        self.assertIsInstance(prestamos, list)
        for p in prestamos:
            self.assertIsInstance(p, Prestamo)
            self.assertTrue(hasattr(p, "nie"))
            self.assertTrue(hasattr(p, "isbn"))

    def test_marcar_como_devuelto(self):
        prestamos = DataManager.get_data("prestamos")
        activos = [p for p in prestamos if p.estado == "P"]

        if not activos:
            self.skipTest("No hay préstamos activos para probar.")

        p = activos[0]
        original_estado = p.estado
        p.marcar_como_devuelto()
        DataManager.guardar([pr.to_dict() for pr in prestamos], "prestamos")

        recargado = DataManager.get_data("prestamos")[0]
        self.assertEqual(recargado.estado, "D")


        recargado.estado = original_estado
        DataManager.guardar([pr.to_dict() for pr in prestamos], "prestamos")

    def test_registrar_prestamo_temporal(self):
        alumnos = DataManager.get_data("alumnos")
        libros = DataManager.get_data("libros")
        cursos = DataManager.get_data("cursos")

        if not alumnos or not libros or not cursos:
            self.skipTest("No hay datos para probar.")
        
        nie = alumnos[0].nie
        isbn = libros[0].isbn
        curso = cursos[0].curso

        prestamos = DataManager.get_data("prestamos")
        clave = (nie, isbn, curso)
        if any((p.nie, p.isbn, p.curso) == clave for p in prestamos):
            self.skipTest("El préstamo ya existe, no se puede duplicar")

        nuevo = Prestamo(nie, curso, isbn, "2024-10-01", "2025-06-15", "P")
        prestamos.append(nuevo)
        DataManager.guardar([p.to_dict() for p in prestamos], "prestamos")

        recargado = DataManager.get_data("prestamos")
        existe = any((p.nie, p.isbn, p.curso) == clave for p in recargado)
        self.assertTrue(existe)

        # Eliminamos el prestamo

        limpio = [p for p in recargado if (p.nie, p.isbn, p.curso) != clave]
        DataManager.guardar([p.to_dict() for p in limpio], "prestamos")


    def test_modificar_estado(self):
        prestamos = DataManager.get_data("prestamos")
        activos = [p for p in prestamos if p.estado == "P"]
        if not activos:
            self.skipTest("No hay préstamos activos para probar.")

        p = activos[0]
        original_estado = p.estado
        p.estado = "D"
        DataManager.guardar([x.to_dict() for x in prestamos], "prestamos")

        actualizado = DataManager.get_data("prestamos")[0]
        self.assertEqual(actualizado.estado, "D")

        actualizado.estado = original_estado
        DataManager.guardar([x.to_dict() for x in prestamos], "prestamos")


    def test_borrar_prestamo(self):
        clave = ("12345678A", "9999999999999", "1ESO")

        prestamos = DataManager.get_data("prestamos")

        # Eliminar el préstamo concreto
        actualizados = [p for p in prestamos if (p.nie, p.isbn, p.curso) != clave]
        DataManager.guardar([p.to_dict() for p in actualizados], "prestamos")

        # Verificar que no está
        recargado = DataManager.get_data("prestamos")
        self.assertFalse(any(
            str(p.nie) == clave[0] and
            str(p.isbn) == clave[1] and
            str(p.curso) == clave[2]
            for p in recargado
        ))


        # Restaurar
        eliminado = Prestamo(*clave, "2024-09-01", "2025-06-01", "P")
        recargado.append(eliminado)
        DataManager.guardar([p.to_dict() for p in recargado], "prestamos")





    def test_cerrar_prestamo_valido(self):
        prestamos = DataManager.get_data("prestamos")
        if not prestamos:
            self.skipTest("No hay préstamos")

        nie = prestamos[0].nie
        todos_alumno = [p for p in prestamos if p.nie == nie]
        for p in todos_alumno:
            p.estado = "D"
        DataManager.guardar([p.to_dict() for p in prestamos], "prestamos")

        # todos deberían estar como devueltos
        actualizado = DataManager.get_data("prestamos")
        devueltos = [p for p in actualizado if p.nie == nie and p.estado != "D"]
        self.assertEqual(len(devueltos), 0)


    def test_firmar_contrato_crea_archivo(self):
        nie = "12345678A"
        ruta = os.path.join("data", f"contrato_{nie}.txt")

        if os.path.exists(ruta):
            os.remove(ruta)
        
        firmar_contrato(nie)
        
        self.assertTrue(os.path.exists(ruta))
        os.remove(ruta)


    def test_cambiar_curso_prestamos(self):
        prestamos = DataManager.get_data("prestamos")
        if not prestamos:
            self.skipTest("No hay préstamos")

        nie = prestamos[0].nie
        nuevo_curso = "PRUEBA_CURSO"

        for p in prestamos:
            if p.nie == nie:
                p.curso = nuevo_curso
        DataManager.guardar([p.to_dict() for p in prestamos], "prestamos")

        verificados = [p for p in DataManager.get_data("prestamos") if p.nie == nie]
        self.assertTrue(all(p.curso == nuevo_curso for p in verificados))









if __name__ == '__main__':
    unittest.main()
