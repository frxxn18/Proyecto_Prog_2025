import unittest

def main():
    carga = unittest.TestLoader()
    carpeta = carga.discover("tests")

    run = unittest.TextTestRunner()
    run.run(carpeta)

    if __name__ == "__main__":
        main()