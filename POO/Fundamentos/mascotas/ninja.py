class Ninja():
    def __init__( self, nombre, apellido, premios, comida_mascota, mascota ):
        self.nombre = nombre
        self.apellido = apellido
        self.premios = premios
        self.comida_mascota = comida_mascota
        self.mascota = mascota

    def caminar(self):
        self.mascota.jugar()
        return self

    def alimentar(self):
        if len(self.comida_mascota) > 0:
            comida = self.comida_mascota.pop()
            print(f"alimentar {self.mascota.nombre} {comida}")
            self.mascota.comer()
        else:
            print("Oh no!! necesita más comida de mascotas!")
        return self

    def bañar(self):
        self.mascota.sonido()
