num1 = 42 #variable de declaración / variable entera 
num2 = 2.3 #variable tipo desimal
boolean = True # dato booleano verdadero y falso
string = 'Hello World' # cadena 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #arreglo tipo lista
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable tipo diccionario
fruit = ('blueberry', 'strawberry', 'banana') # tupla (que no cambio, lista inmutable)
print(type(fruit)) #imprimir o mostrar (imprimira la tupla)
print(pizza_toppings[1]) #imprimir o mostrar, posicion n1 (sausage)
pizza_toppings.append('Mushrooms') #agregar 
print(person['name']) #agregar valor 
person['name'] = 'George' #agregar dato
person['eye_color'] = 'blue' #agregar dato
print(fruit[2]) #imprimir segunda posicion (banana)


if num1 > 45: #condicional (si)
    print("It's greater") #imprimir
else: #condicional (si no)
    print("It's lower") #imprimir

if len(string) < 5: #condicional (si)
    print("It's a short word!") #imprimir
elif len(string) > 15: 
    print("It's a long word!")
else: #condicional (si no )
    print("Just right!") #imprimir 

for x in range(5): #for en un rango de 0 a 5
    print(x) #imprimir x
for x in range(2,5): #for en un rango de 0 a 2
    print(x) #imprimir x
for x in range(2,10,3): #for en un rango de 2 a 10 a 3 (?
    print(x) #imprimir
x = 0 # x es igual a 0
while(x < 5):
    print(x) #imprimir 
    x += 1 

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person) #imprimir person
person.pop('eye_color') #eliminar elemento eye color de la variable person
print(person) #volver a imprimir person

for topping in pizza_toppings: #bucle topping en pizza_toppings
    if topping == 'Pepperoni': #si tooping es igual a pepperoni seguir
        continue
    print('After 1st if statement') #imprimir 
    if topping == 'Olives': #si toopping es igual a olives terminar
        break

def print_hello_ten_times(): #definir variable 
    for num in range(10): #for en un rango de 0 a 10
        print('Hello') #imprimir 

print_hello_ten_times()

def print_hello_x_times(x): #definir variable
    for num in range(x): 
        print('Hello') #imprimir

print_hello_x_times(4) 

def print_hello_x_or_ten_times(x = 10): #definir variable 
    for num in range(x): #for en un rango de 0 a x (10)
        print('Hello') #imprimir

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)