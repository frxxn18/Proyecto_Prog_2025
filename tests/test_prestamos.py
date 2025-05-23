import unittest
from utils.DataManager import DataManager
from models.prestamo import Prestamo

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

if __name__ == '__main__':
    unittest.main()
