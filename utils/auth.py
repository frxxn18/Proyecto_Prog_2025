#aqui iran funciones para el login y el logout

USUARIO = "fran"
CONTRASEÑA = "123"

def login():
    print("--Inicio de sesion--")
    usuario = input("Ingrese el usuario: ").strip()
    constraseña = input("Ingrese la contraseña: ").strip()
    if usuario == USUARIO and constraseña == CONTRASEÑA:
        print("Sesion iniciada")
        return True
    else:
        print("Usuario o contraseña incorrectos")
        return False
    

def logout():
    print("Se ha cerrado la sesion correctamente")
