class Mascota:
    def __init__( self, name, tipo, golosinas ):
        self.name = name
        self.tipo = tipo 
        self.golosinas = golosinas
        self.salud = 100
        self.energia = 100

    def dormir(self):
        self.energia += 25
        return self

    def comer(self):
        self.energia += 5
        self.salud += 10

    def jugar(self):
        self.salud += 5
        self.energia -= 15
        return self

    def sonido(self):
        print(self.sonido)

    def MostrarEnergia(self):
        print(f"La energia de kitty es: {self.energia}")
        return self

    def MostrarSalud(self):
        print(f"La salud de kitty es: {self.salud}")
        return self