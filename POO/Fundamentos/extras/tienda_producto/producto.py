class Producto:
    def __init__(self, nombre, precio, categoria): #atributos
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        if esta_elevado: 
            self.precio += self.precio * cambio_porcentaje /100

        else:
            self.precio -= self.precio * cambio_porcentaje /100
        return self

    def imprimir_info(self):
        print(f"---El nombre del producto es: {self.nombre} ---La categoria es: {self.categoria} ---El precio del producto es: {self.precio}")
        return self

"""
    producto1 = Producto("Confort", 1200, "higiene") #texto con "" y números sin ""
    producto1.imprimir_info() #se llama al def donde ya teniamos el print 
    producto2 = Producto("Trencito", 1400 , "Chocolate")
    producto2.imprimir_info()
"""