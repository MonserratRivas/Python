#básico
for x in range(0,151):
    print(x)


#multiplos de 5
for y in range(5,1001,5):
    print(y)


#contando al estilo dojo
for a in range(0,101):
    if a % 5 == 0:
        print("Coding")

    elif a % 10 == 0:
        print("Coding Dojo")

    else:
        print(a)


#whoa. Es un gran idiota
for n in range(0,500001,3):
    print(n)


#cuenta regresiva de 4
count = 2018
while count >= 0:
    print(count)
    count -= 4


#contador flexible
lowNum = 2
highNum = 9
mult = 3
for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)
