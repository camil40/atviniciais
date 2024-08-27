class Carro:
    def __init__(self, consumo, combustivel=0):
        self.consumo = consumo
        self.combustivel = combustivel

    def Andar(self, distancia):                                                                   
        return self.combustivel - distancia/self.consumo
    
    def obterGasolina(self):
        return self.combustivel
    
    def adicionarGasolina(self, novoCombustivel):
        self.combustivel = self.combustivel + novoCombustivel
        return self.combustivel
    
fusca = Carro(15) 
print(fusca.adicionarGasolina(20))
print(fusca.Andar(100))
print(fusca.obterGasolina())