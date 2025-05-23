import unittest
import os
from utils.DataManager import DataManager

class TestDatos(unittest.TestCase):

    def test_cargar_todas_las_tablas(self):
        tablas = ["alumnos", "cursos", "materias", "libros", "prestamos"]
        for tabla in tablas:
            with self.subTest(tabla=tabla):
                datos = DataManager.get_data(tabla)
                self.assertIsInstance(datos, list)

    def test_exportar_json(self):
        alumnos = DataManager.cargar("alumnos")
        export_path = "alumnos_test_export.json"
        try:
            with open(export_path, "w", encoding="utf-8") as f:
                import json
                json.dump(alumnos, f, indent=4, ensure_ascii=False)
            self.assertTrue(os.path.exists(export_path))
        finally:
            if os.path.exists(export_path):
                os.remove(export_path)

    def test_creacion_backup(self):
        import json
        backup_folder = "backup_test"
        os.makedirs(backup_folder, exist_ok=True)
        alumnos = DataManager.cargar("alumnos")
        ruta = os.path.join(backup_folder, "alumnos_back.json")
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(alumnos, f, indent=4, ensure_ascii=False)
        self.assertTrue(os.path.exists(ruta))
        # Limpiar
        os.remove(ruta)
        os.rmdir(backup_folder)

if __name__ == '__main__':
    unittest.main()
