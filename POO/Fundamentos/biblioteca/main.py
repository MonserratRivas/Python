from libro import Libro
from usuario import Usuario
from biblioteca import Biblioteca

def mostra_menu():
    print("\n \t ---Menú--- \n")
    print("Opción 1: Agregar libro a Biblioteca")
    print("Opción 2: Eliminar libro de Biblioteca")
    print("Opción 3: Tomar prestado libro de Biblioteca")
    print("Opción 4: Devolver libro a Biblioteca")
    print("Opción 5: Crear nuevo Usuario")
    print("Opción 6: Eliminar Usuario")
    print("Opción 7: Ver lista de libros en Biblioteca")
    print("Opción 8: Ver lista de Usuarios ")
    print("Opción 0: Salir \n")

while True:
    mostra_menu()
    Option = input("\t Escoja una opción: \n")

    if Option == "1":
        print("\t -Agregar libro a Biblioteca.- \n")
        titulo = input("Ingrese el titulo del libro: ")
        autor = input("Ingrese al autor del libro: ")
        año_publicacion = input("Ingrese el año de publicación del libro: \n")
        print("\t -Nuevo libro agregado exitosamente.- \n")

    elif Option == "2":
        print("\t -Eliminar libro de Biblioteca.- \n")
        titulo = input("Ingrese nombre del libro deseado: ")
        print(input(f"¿Eliminar libro: {titulo} de la Biblioteca? /si /no: "))
        print("\t -Libro eliminado exitosamente.- \n")

    elif Option =="3":
        print("\t -----Tomar prestado libro de Biblioteca.----- \n")
        titulo = input("Ingrese nombre del libro: ")
        tiempo = input(f"Seleccione la cantidad de tiempo que tendra el libro {titulo}: ")
        print(f"El libro {titulo} debe ser devuelto en {tiempo}. \n")
        Usuario.tomar_prestado()
        print("\t -Prestamo de libro exitoso.- \n")

    elif Option == "4":
        print("\t -----Devolver libro.----- \n")
        Usuario.devolver_libro()
        titulo = input("Ingrese el nombre del libro: ")

    elif Option == "5":
        print("\t -----Crear nuevo Usuario.----- \n")
        nombre = input("Ingrese nombre de Usuario: ")
        id_user = input("Ingrese el ID de Usuario: ")
        print("\t -Nuevo Usuario creado.- \n")

    elif Option == "6":
        print("\t -----Eliminar Usuario.----- \n")
        nombre = input("Ingrese nombre de Usuario: ")
        id_user = input("Ingrese el ID de la cuenta: ")

    elif Option == "7":
        print("\t -Lista de libros.- \n")

    elif Option == "8":
        print("\t -Lista de Usuarios.- \n")

    elif Option == "0":
        print("¡Hasta luego!")
        break

    else: 
        print("\t Opción invalida. Intente nuevamente \n")
