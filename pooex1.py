class Triangulo:
    def __init__(self, LadoA, LadoB, LadoC):
        self.LadoA = LadoA
        self.LadoB = LadoB
        self.LadoC = LadoC

    def Perimetro(self):
        return self.LadoA + self.LadoB + self.LadoC
    
    def MaiorLado(self):
        maiorLado = None
        if self.LadoA > self.LadoB and self.LadoA > self.LadoC:
            maiorLado = self.LadoA
        elif self.LadoB > self.LadoA and self.LadoB > self.LadoC:
            maiorLado = self.LadoB
        elif self.LadoC > self.LadoA and self.LadoC > self.LadoB:
            maiorLado = self.LadoC
        else:
            maiorLado = "Todos os lados são iguais"
        
        return maiorLado
    
triangulo = Triangulo(13, 10, 15)
print("O perimetro é:",triangulo.Perimetro(),"\nO maior lado é:",triangulo.MaiorLado())