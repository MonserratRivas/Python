class Usuario:
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.balance_cuenta = 0

Usuario()
guido = Usuario()
monty = Usuario()
print(guido.name)
print(monty.name)

class Usuario:
    # declarando un atributo de clase
    nombre_banco = "Primer Dojo Nacional"		
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.balance_cuenta = 0

guido = Usuario()
monty = Usuario()
guido.nombre_banco = "Dojo Credit Union"
print(guido.nombre_banco) # salida: Dojo Credit Union 
print(monty.nombre_banco) # salida: Primer Dojo Nacional

class Usuario:
    nombre_banco = "Primer Dojo Nacional"
    def __init__(self , name, email_address, balance_cuenta):
        self.name = name
        self.email = email_address
        self.balance_cuenta = 0
    def hacer_depósito(self, amount):
    	self.balance_cuenta += amount

carlos = Usuario("Carlos", "carlos@python.com")
catalina = Usuario("Cata", "catalina@python.com")
naomi = Usuario("Naomi", "naomi@python.com")
javiera = Usuario("Javiera", "javi@python.com")
matias = Usuario("Matias", "mati@python.com")

carlos.hacer_depósito(100)
catalina.hacer_depósito(2000)

print(f"Mi nombre es {carlos.name} , mi correo es {carlos.email} y mi cuenta bancaria es de {carlos.balance_cuenta}")
print(f"Mi nombre es {catalina.name} , mi correo es {catalina.email} y mi cuenta bancaria es de {catalina.balance_cuenta}")
print(f"Mi nombre es {naomi.name} y mi correo es {naomi.email}")
print(f"Mi nombre es {javiera.name} y mi correo es {javiera.email}")
print(f"Mi nombre es {matias.name} y mi correo es {matias.email}")


class CuentaBancaria:
    # atributo de clase
    nombre_banco = "Primer Dojo Nacional"
    todas_las_cuentas = []
    def __init__(self, int_rate,balance):
        self.tasa_int = tasa_int
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)
    
    # método de clase para cambiar el nombre del banco
    @classmethod
    def cambiar_nombre_banco(cls,name):
        cls.nombre_banco = name
    # método de clase para obtener balance de todas las cuentas
    @classmethod
    def todos_los_balances(cls):
        sum = 0
        # utilizamos cls para referirnos a la clase 
        for account in cls.todas_las_cuentas:
            sum += balance.cuenta
        return sum