class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def AumentarSalario(self, percentualDeAumento):
        return self.salario * (percentualDeAumento/100 + 1)
    
f1 = Funcionario("Maria", 2500)
print(f1.AumentarSalario(10))