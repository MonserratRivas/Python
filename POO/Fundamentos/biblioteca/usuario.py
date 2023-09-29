class Usuario:
    def __init__(self, nombre, id_user, libros_prestados):
        self.nombre = nombre
        self.id_user = id_user
        self.libros_prestados = libros_prestados
        self.list = []

    def tomar_prestado(self):
        for a in self.list:
            if a.libro == tomar_prestado:
                a.remove(eliminar_libro_biblioteca)
            else: 
                print("El libro seleccionado no existe. ")
                return self

    def devolver_libro(self):
        self.list.append(agregar_libro)
        return self