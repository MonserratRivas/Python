class Usuario:
    def __init__(self, nombre, apellido, correo, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo 
        self.contraseña = contraseña 

    def cambiarNombre(self):
        self.usuario.cambiarNombre()
        return self

    def cambiarContraseña(self):
        self.usuario.cambiarContraseña()
        return self

    def cerrarSesion(self):
        self.usuario.cerrarSesion()
        return self