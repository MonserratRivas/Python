class Administrador:
    def __init__(self, usuarios):
        self.usuarios = usuarios

    def agregarUser(self):
        self.usuarios.agregarUser()
        self.invitado.agregarUser()
        return self

    def eliminarUser(self):
        self.usuarios.eliminarUser()
        self.invitado.eliminarUser()
        return self

    def editarUser(self):
        self.usuarios.editarUser()
        self.invitado.editarUser()
        return self