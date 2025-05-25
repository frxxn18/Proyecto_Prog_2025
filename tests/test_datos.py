import unittest
import os
from utils.DataManager import DataManager
import json
import pandas as pd

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
        backup_carpeta = "backup_test"
        os.makedirs(backup_carpeta, exist_ok=True)
        alumnos = DataManager.cargar("alumnos")
        ruta = os.path.join(backup_carpeta, "alumnos_back.json")
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(alumnos, f, indent=4, ensure_ascii=False)
        self.assertTrue(os.path.exists(ruta))
        # Limpiar
        os.remove(ruta)
        os.rmdir(backup_carpeta)


    def test_exportar_datos_alumnos_json(self):
        alumnos = DataManager.cargar("alumnos")
        export_ruta = "alumnos_export_test.json"
        
        try:
            with open(export_ruta, "w", encoding="utf-8") as f:
                json.dump(alumnos, f, indent=4, ensure_ascii=False)
            self.assertTrue(os.path.exists(export_ruta))
        finally:
            if os.path.exists(export_ruta):
                os.remove(export_ruta)


    def test_exportar_datos_libros_csv(self):
        libros = DataManager.cargar("libros")
        export_path = "libros_export_test.csv"
        
        try:
            pd.DataFrame(libros).to_csv(export_path, index=False)
            self.assertTrue(os.path.exists(export_path))
        finally:
            if os.path.exists(export_path):
                os.remove(export_path)


    def test_vaciar_y_restaurar_datos_temporalmente(self):
        tablas = ["alumnos", "cursos", "materias", "libros", "prestamos"]
        copia_original = {}

        # Guardar copia de seguridad
        for tabla in tablas:
            copia_original[tabla] = DataManager.cargar(tabla)

        # Vaciar
        DataManager.vaciar_base(tablas)
        for tabla in tablas:
            vaciado = DataManager.cargar(tabla)
            self.assertEqual(vaciado, [])

        # Restaurar
        for tabla in tablas:
            DataManager.guardar(copia_original[tabla], tabla)



if __name__ == '__main__':
    unittest.main()
