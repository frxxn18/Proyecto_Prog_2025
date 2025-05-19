from menus.menu_principal import mostrar_menu_principal
from utils.auth import login, logout

def main():
    print("Bienvenido al sistema de gestión de libros")
    if login():
        mostrar_menu_principal()
        logout()
    else:
        print("Sesión no iniciada")
        input("Pulsa ENTER para continuar.")

if __name__ == "__main__":
    main()
