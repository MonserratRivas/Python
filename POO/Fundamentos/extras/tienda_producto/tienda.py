class Tienda:
    def __init__(self, nombre): #atributos
        self.nombre = nombre
        self.lista = []
        
    def agregar_producto(self, nuevo_producto): 
        self.lista.append(nuevo_producto)
        return self

    def vender_producto(self, id):
        for x in self.lista:
            if x.nombre == id:
                x.remove
            else: 
                print("El producto no existe.")
        return self

    def listar_productos(self):
        for x in self.lista:
            x.imprimir_info()
        return self


    def actualizar_producto(self, producto):
        for x in self.lista:
            if x.nombre == id:
                x.nombre = producto.nombre
                x.precio = producto.precio
                x.categoria = producto.categoria
                print("--El producto se modifico correctamente--")
            else: 
                print("El producto no existe.")
        return self


    def inflación(self, porcentaje_aumento): 
        pass

    def hacer_liquidación(self, category, porcentaje_descuento): 
        pass