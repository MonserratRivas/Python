from sistema import Sistema
from administrador import Administrador
from usuario import Usuario
from invitado import Invitado

def mostrar_menu():
    print("----Menú----")
    print("Option 1: Ingresar")
    print("Opcion 2: Editar")
    print("Opcion 3: Borrar ")
    print("Opcion 4: listar ")
    print("Opcion 0: Salir")

while True:
    mostrar_menu()
    system = Sistema()
    Option = input("Escoga una opción: ")

    if Option == "1":
        print("+-------------------------------------+")
        print("|         Crear nuevo Usuario         |")
        print("+-------------------------------------+")
        nombre = input("Escriba su nombre de Usuario aqui:")
        correo = input("Ingrese su correo aqui:")
        contraseña = input("Cree una contraseña: ")
        print("+-------------------------------------+")
        print("|        Nuevo Usuario creado         |")
        print("+-------------------------------------+")

        usuario = usuario(nombre_nuevo, correo_nuevo, contraseña_nueva)
        system.registrarUsuarios(usuario)
            
    elif Option == "2":
        print("+-------------------------------------+")
        print("|      Editar perfil de Usuario       |")
        print("+-------------------------------------+")
        nombre_nuevo = input("Escriba su nuevo nombre de Usuario: ")
        correo_nuevo = input("Escriba su nueva correo electronico: ")
        contraseña_nueva = input("Escriba su nueva contraseña: ")
        print("+-------------------------------------+")
        print("|      Nueva contraseña guardada      |")
        print("+-------------------------------------+")

    elif Option == "3":
        print("+-------------------------------------+")
        print("|     Eliminar perfil de Usuario      |")
        print("+-------------------------------------+")

    elif Option == "4": 
        print("+-------------------------------------+")
        print("|      Editar perfil de Usuario       |")
        print("+-------------------------------------+")

    elif Option == "0": 
        break
