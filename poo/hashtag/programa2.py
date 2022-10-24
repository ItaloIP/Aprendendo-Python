class Clientes:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf


cliente1 = Clientes('José', 35, '350-639-476-20')
cliente2 = Clientes('Italo', 16, '161-107-966-70')

print(cliente1.cpf)