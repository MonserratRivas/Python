from calcular import Calculadora

def mostrar_menu():
    print("-----Calculadora-----")
    print("Opción 1: Sumar")
    print("Opción 2: Restar")
    print("Opción 3: Dividir")
    print("Opción 4: Multiplicar")
    print("Opción 5: Salir")

calculadora = Calculadora(0, 0)

while True:
    mostrar_menu()
    Option = input("Escoja una opción: ")

    if Option == "1":
        print("Sumar")
        n1 = float(input("Ingrese el primer números que desee sumar: "))
        n2 = float(input("Ingrese el segundo número que desee sumar: "))
        Resultado = calculadora.Sumar(n1, n2)
        print(f"--------El resultado de la suma es: {Resultado}\n")

    elif Option == "2":
        print("Restar")
        n1 = float(input("Ingrese el primer números que desee restar: "))
        n2 = float(input("Ingrese los números que desee restar:"))
        Resultado = calculadora.Restar(n1, n2)
        print(f"-------El resultado de la resta es: {Resultado}\n")

    elif Option == "3":
        print("Multiplicar")
        n1 = float(input("Ingrese el primer números que desee multiplicar: "))
        n2 = float(input("Ingrese los números que desee multiplicar: "))
        Resultado = calculadora.Multiplicar(n1, n2)
        print(f"--------El resultado de la división es: {Resultado}\n")

    elif Option == "4":
        print("Dividir")
        n1 = float(input("Ingrese el primer números que desee dividir: "))
        n2 = float(input("Ingrese los números que desee dividir: "))
        Resultado = calculadora.Dividir(n1, n2)
        print(f"--------El resultado de la visión es: {Resultado}\n")

    elif Option == "0":
        print("¡Hasta luego!")
        break

    else:
        print("Opción invalida. Intente nuevamente. \n")