class SList:
    def __init__(self):
        self.head = None
    def add_to_front(self, val):	# agregó esta línea, toma un valor

        def add_to_front(self, val):
            new_node = SLNode(val)	# crea una nueva instancia de nuestra clase Node usando el valor dado

class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None
    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head	# guarda el encabezado actual en una variable

	def add_to_front(self, val):
            new_node = SLNode(val)
            current_head = self.head
            new_node.next = current_head	# ESTABLECE el nuevo nodo JUNTO AL encabezado actual de la lista

	def add_to_front(self, val):
            new_node = SLNode(val)
            current_head = self.head
            new_node.next = current_head
            self.head = new_node	# FIJA el encabezado de la lista AL nodo que creamos en el último paso
            return self	 # return self para permitir el encadenamiento

	def print_values(self):
	def print_values(self):
            runner = self.head	# un puntero al primer nodo de la lista
	def print_values(self):
            runner = self.head
            while (runner != None):	# iterando mientras runner es un nodo y no None
</div>
	def print_values(self):
            runner = self.head
            while (runner != None):
                print(runner.value)	# imprime el valor del nodo actual
	def print_values(self):
            runner = self.head
            while (runner != None):
                print(runner.value)
                runner = runner.next 	# establece runner a su vecino
            return self	# una vez terminado el ciclo, devuelve self para permitir el encadenamiento
	def add_to_back(self, val):	# acepta un valor
	def add_to_back(self, val):
        new_node = SLNode(val)	# crea una nueva instancia de nuestra clase Node con el valor dado</span></
	def add_to_back(self, val):
        new_node = SLNode(val)
        runner = self.head	# establecer un iterador para que comience al principio de la lista
	def add_to_back(self, val):
            new_node = SLNode(val)
            runner = self.head
            while (runner.next != None):	# iterador hasta que el iterador no tenga un vecino
	def add_to_back(self, val):
            new_node = SLNode(val)
            runner = self.head
            while (runner.next != None):
                runner = runner.next # incrementa runner al siguiente nodo de la lista
	def add_to_back(self, val):
            new_node = SLNode(val)
            runner = self.head
            while (runner.next != None):
                runner = runner.next
            runner.next = new_node	# incrementa runner al siguiente nodo de la lista
	def add_to_back(self, val):
            if self.head == None:	# si la lista está vacía
                self.add_to_front(val)	# ejecuta el método add_to_front
            return self	# asegurémonos de que el resto de esta función no suceda si agregamos al comienzo
                new_node = SLNode(val)
                runner = self.head
            while (runner.next != None):
                runner = runner.next
                runner.next = new_node	# incrementa runner al siguiente nodo de la lista
            return self # return self para permitir el encadenamiento

my_list = SList()	# crea una nueva instancia de una lista
my_list.add_to_front("son").add_to_front("Las listas enlazadas").add_to_back("divertidas!").print_values()  # encadenando, yeah!
# la salida debería ser:
# Las listas enlazadas
# son
# divertidas!












