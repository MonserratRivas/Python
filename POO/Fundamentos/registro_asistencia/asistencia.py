class SistemaAsistencia:
    def __init__(self, usuario, registro):
        self.usuario = usuario
        self.registro = registro

    def listar_registros(self):
        self.usuario.registro.listar_registros()