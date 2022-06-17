class MathDojo:
    def __init__(self):
        self.resultado = 0

    def sumar(self, num, *nums):
        self.resultado += num
        for elementos in nums:
            self.resultado += elementos
        return self
    
    def restar(self, num, *nums):
        self.resultado -= num
        for elementos in nums:
            self.resultado -= elementos
        return self
    
    def resultado(self):
        return self.resultado

md = MathDojo()
x = md.sumar(2, 5, 1).sumar(2).restar(3, 2).resultado
print(x)