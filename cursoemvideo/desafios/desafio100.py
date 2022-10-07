from random import randint

def Sortear(lista):
    """
    -> Sortea números e adiciona na lista
    :param lista: Pega o valor referente a lista no programa principal.
    :return: sem retorno
    Função criada por Italo
    """
    for c in range(0,5):
        lista.append(randint(1,10))
    print(f'Números sorteados! {lista}')
    print()

def SomaPar(listaa):
    par = 0
    print(f'Somando os números pares da lista: {listaa}')
    for b, a in enumerate(listaa):
        if a % 2 == 0:
            par += a
    print(f'Resultado: {par}')



#Programa Principal
numeros = []
Sortear(numeros)
SomaPar(numeros)
help(Sortear)
