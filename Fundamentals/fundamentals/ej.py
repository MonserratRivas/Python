dic_vacío = {}
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
print(ensalada)

