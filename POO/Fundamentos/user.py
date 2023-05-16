class Usuario:
    nombre_banco = "hola"
    def __init__(self , balance_cuenta):
        self.balance_cuenta = 10000
    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount
    def hacer_depósito(self, amount):
        self.balance_cuenta += amount

Catalina = Usuario("balance_cuenta")
Naomi = Usuario("balance_cuenta")
Javiera = Usuario("balance_cuenta")

Catalina.hacer_depósito(100)
Catalina.hacer_depósito(40)
Catalina.hacer_depósito(3000)
Catalina.hacer_retiro(200)

Naomi.hacer_depósito(300)
Naomi.hacer_depósito(560)
Naomi.hacer_retiro(250)
Naomi.hacer_retiro(680)

Javiera.hacer_depósito(4050)
Javiera.hacer_retiro(360)
Javiera.hacer_retiro(280)
Javiera.hacer_retiro(780)

print(f"Catalina, Balance: {Catalina.balance_cuenta}")
print(f"Naomi, Balance: {Naomi.balance_cuenta}")
print(f"Javiera, Balance: {Javiera.balance_cuenta}")