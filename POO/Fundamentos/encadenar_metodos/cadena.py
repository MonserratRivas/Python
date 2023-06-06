class Usuario:
    nombre_banco = "hola"
    def __init__(self , balance_cuenta):
        self.balance_cuenta = 10000
        return self

    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount
        return self

    def hacer_depósito(self, amount):
        self.balance_cuenta += amount
        return self

Catalina = Usuario("balance_cuenta")
Naomi = Usuario("balance_cuenta")
Javiera = Usuario("balance_cuenta")

Catalina.hacer_depósito(100).Catalina.hacer_depósito(40).Catalina.hacer_depósito(3000).Catalina.hacer_retiro(200)

print(f"Catalina, Balance: {Catalina.balance_cuenta}")
