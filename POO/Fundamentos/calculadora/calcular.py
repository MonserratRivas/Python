class Calculadora:
    resultados = []
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
        self.operacion = ""


    def Sumar(self, n1, n2):
        self.operacion = f"{n1} + {n2}"
        return n1 + n2

    def Restar(self, n1, n2):
        self.operacion = f"{n1} + {n2}"
        return n1 - n2

    def Multiplicar(self, n1, n2):
        self.operacion = f"{n1} * {n2}"
        return n1 * n2

    def Dividir(self, n1, n2):
        if n2 != 0:
            self.operacion = f"{n1} / {n2}"
            return n1 / n2
        else: 
            return "Error: No se puede dividir entre cero."