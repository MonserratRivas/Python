from producto import Producto
from tienda import Tienda

def mostrar_menu():
    print("------Tienda------")
    print("Option 1: Registrar Nuevo producto")
    print("Opcion 2: Registrar una venta")
    print("Opcion 3: Listar Productos ")
    print("Opcion 0: Salir")

def main():
    tienda1 = Tienda("Tienda de Cata")
    while True:
        mostrar_menu()
        Option = input("Escoja una Opcion: ")
        if Option == "1":
            nombre = input("Ingrese el nombre del producto: ")
            precio = input("Ingrese el precio del producto: ")
            categoria = input("Ingrese la categoria del producto: ")
            
            nuevo_producto = Producto(nombre, precio, categoria)
            tienda1.agregar_producto(nuevo_producto)
            print("-----Producto Creado-----")
        if Option == "2":
            pass
        elif Option == "3":
            tienda1.listar_productos()
        elif Option == "0":
            pass 
        else: 
            pass

if __name__== "__main__":
    main()
