class Produto:
    qtdProd = 0
    def __init__(self, cod, preco):
        self.__cod = cod
        self.__preco = preco
        Produto.qtdProd += 1

    def getPreco(self):
        return self.__preco
    

    def setPreco(self, preco):
        self.__preco = preco
        return self.__preco
    
    def getCod(self):
        return self.__preco
    
    def setCod(self, cod):
        self.__cod = cod
        return self.__cod


prod1 = Produto(1, '10')
print(prod1.getCod())
print(prod1.qtdProd)

prod2 = Produto(2, '15')
print(prod2.getCod())
print(prod2.qtdProd)


class GerenciarProdutos:
    listaprod = []
    def __init__(self):
        self.listaprod = []

    def getList(self):
        for i in self.listaprod:
            print(f"Preço: {i.getPreco()}, Código: {i.getCod_prod()}")

    def AdicionarProduto(self, prod):
        self.listaprod.append(prod)
        return self.listaprod()

    def RemoverProduto(self, cod__prod):
        for pro in self.listaprod:
            if cod__prod == pro.getcod():
                self.listaprod.remove(pro)

    def PrecoTotal(listacod):
        precototal = 0
        for i in self.listaprod:
            if listacod == i.getcod():
                precototal += self.listaprod



p1 = Produto(15, 123)
p2 = Produto(16, 1234)
p3 = Produto(17, 12345)

gerenciador = GerenciarProdutos()

print(gerenciador.AdicionarProduto(p1))


