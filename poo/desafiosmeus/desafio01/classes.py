class Produtos:
    def __init__(self, nome, preço = 0, unidades = 0):
        self.nome = nome
        self.preço = preço
        self.unidades = unidades
        

    def Reposicao(self, num):
        if num < 0:
            print('Reposição impossível')
        else:
            self.unidades += num


    def NewPrice(self, price):
        self.preço = price


    def Comprar(self, uni):
        if self.unidades < uni:
            print('Compra Impossível')
        else:
            self.unidades -= uni

