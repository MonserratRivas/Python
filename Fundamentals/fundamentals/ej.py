"""dic_vacío = {}
new_person = {'name': 'John', 'edad': 38, 'peso': 160.2, 'usa_lentes': False}
new_person['name'] = 'Jack'	# actualiza si la llave existe, agrega un par clave-valor si no
new_person['hobbies'] = ['escalada', 'programación']
print(new_person)	
# salida: {'name': 'Jack', 'edad': 38, 'peso: 160.2, 'usa_lentes': False, 'hobbies': ['escalada', 'programación']}
# w = new_person.pop('peso')	# remueve la llave indicada y devuelve el valor
# print(w)		# salida: 160.2
# print(new_person)	
# # salida: {'name': 'Jack', 'edad': 38, 'usa_lentes': False, 'hobbies': ['escalada', 'programación']}    


print(type(2.63))		# salida: <class 'float'>
print(type(new_person))		# salida: <class 'dict'>


print(len(new_person))		# salida: 4 (el número de pares clave-valor)
print(len('Coding Dojo'))	# salida: 11


int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))


first_name = "Zen"
last_name = "Coder"
age = 27
print(f"Mi nombre is {first_name} {last_name} and tengo {age} años de edad.")


frutas = ['manzana', 'plátano', 'naranja', 'frutilla']
vegetales = ['lechuga', 'pepino', 'zanahorias']
frutas_y_vegetales = frutas + vegetales
print(frutas_y_vegetales)
ensalada = 3 * vegetales
print(ensalada)






frutas = ['manzana', 'plátano', 'naranja', 'frutilla']
vegetales = ['lechuga', 'pepino', 'zanahorias']
frutas_y_vegetales = frutas + vegetales
print(frutas_y_vegetales)
ensalada = 3 * vegetales
print(ensalada)"""


"""for x in range(0, 10, 2):
    print(x)
# salida: 0, 2, 4, 6, 8

for x in 'Hello':
    print(x)
# salida: 'H', 'e', 'l', 'l', 'o'"""


"""mi_lista = ["abc", 123, "xyz"]
for i in range(0, len(mi_lista)):
    print(i, mi_lista[i])
# salida: 0 abc, 1 123, 2 xyz
    
# O 
    
for v in mi_lista:
    print(v)
# salida: abc, 123, xyz"""


# tupla
"""perro = 'martillo','bomba','chiporro','ganado','ganado' /////una tupla puede o no puede usar () no es una exigencia
for data in perro:
    
    print(data)"""


# diccionarios (clave y valor)
"""mi_dicc = { "nombre": "Noelle", "lenguaje": "Python" }
for k in mi_dicc:
    print(k)"""
# salida: nombre, lenguaje

"""
capitales = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# otra forma de iterar a través de las claves
for key in capitales.keys():
    print(key)
# salida: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
# para iterar a través de los valores
for val in capitales.values():
    print(val)
# salida: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# para iterar a través de las claves y valores
for key, val in capitales.items():
    print(key, " = ", val)
# salida: Washington = Olympia, California = Sacramento, Idaho = Boise, etc"""


"""
count = 0
while count <= 5:
    print("looping - ", count)
    count += 1"""

"""
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Sentencia else final")"""

"""
for val in "cadena":
    if val == "e":
        continue
    print(val)
# salida: c, a, d, n, a
# nota: no hay e en el resultado, pero el bucle continuó hasta después de la e """ 


"""
y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
    else:		# solo se ejecuta en una salida limpia del bucle while (es decir, no un break)
        print("sentencia else final")
# salida: 3, 2, 1""" 

"""
new_val = add(3, 5)    # llamar la función con los argumentos 3 y 5
print(new_val)    # el resultado de la función add se devuelve y guarda en new_val, por lo que veremos 8"""






#DI HOLA
"""
def di_hola(nombre):
    print("Hola, " + nombre)
    return "ole" + nombre
val = di_hola('michael')

print(val) """

"""
def di_hola(nombre):
    return "Hola " + nombre
saludo = di_hola("Michael") # el valor devuelto por la función di_hola se asigna a la variable 'saludo'
print(saludo) # esto dará como resultado 'Hola Michael """


# def multiplicar(num_list, num):
#     for x in num_list:
#         x *= num
#     return num_list
# a = [2,4,10,16]
# b = multiplicar(a,5)
# print(b)
# salida:
# [2,4,10,16]
# num1 = 5
# num2 = 7
# num1 = num1 + num2
# print((num1))

import random
print(random.randint(6,10))