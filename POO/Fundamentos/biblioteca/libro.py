class Libro:
    def __init__(self, titulo, autor, año_publicacion, estado):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.estado = estado
        self.list = []

    def devolucion_libro(self):
        self.list.append(agregar_libro)
        return self
