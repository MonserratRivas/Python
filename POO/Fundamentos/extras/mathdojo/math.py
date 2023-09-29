class MathDojo:
    def __init__(self):
        self.result = 0

    def Sumar(self, num, *nums):
        self.result += num
        for z in nums:
            self.result += z
        return self

    def Restar(self, num, *nums):
        self.result -= num
        for b in nums:
            self.result -= b
        return self

md = MathDojo()

x = md.Sumar(2).Sumar(2,5,1).Restar(3,2).result
print(x)

x = md.Sumar(10).Sumar(5,3).Restar(4,3).result
print(x)

a = md.Sumar(200,30,500).Restar(300,67).result
print(a)

q = md.Sumar(4,5,6).result
print(q)