class Usuario:

    nombre_banco = "hola"
    def __init__(self , name):
        #Se asigna el nombre
        self.name = name
        #Se asigna el balance de la cuenta en 0
        self.monto = 0
    def hacer_deposito(self, monto):
        self.monto+=monto
        return self
    def hacer_retiro(self, monto):
        self.monto-=monto
        return self

    def mostrar_balance(self):
        print(f"el saldo de {self.name} es de : {self.monto}")
        return self

Catalina = Usuario("Catalina")
Catalina.hacer_deposito(100)
Catalina.mostrar_balance()
