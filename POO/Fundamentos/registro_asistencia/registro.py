class Registro:
    def __init__(self, usuario, tiempo, entrada, salida):
        self.usuario = usuario
        self.tiempo = tiempo

    def agregar_usuario(self):
        self.usuario.agregar_usuario()

    def registrar_entrada(self):
        self.usuario.entrada.registrar_entrada()

    def registrar_salida(self):
        self.usuario.salida.registrar_salida()

