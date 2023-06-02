from usuario import Usuario
from registro import Registro
from asistencia import SistemaAsistencia

def mostrar_menu():
    print("---Menú Asistencia---")
    print("Opción 1: Registrar nuevo Usuario")
    print("Opción 2: Registrar entrada")
    print("Opción 3: Registrar salida")
    print("Opción 4: Ver registro de Asistencia")
    print("Opción 0: Salir")

while True:
    mostrar_menu()
    Option = input("Escoja una opción: ")

    if Option == "1":
        pass

    elif Option == "2":
        pass

    elif Option == "3":
        pass

    elif Option == "4":
        pass

    elif Option == "0":
        print("¡Hasta luego!")
        break

    else:
        print("Opción invalida. Intente nuevamente. \n")