import unittest

def main():
    print(">>> Ejecutando tests...")
    carga = unittest.TestLoader()
    carpeta = carga.discover("tests")
    run = unittest.TextTestRunner()
    run.run(carpeta)

if __name__ == "__main__":
    main()
