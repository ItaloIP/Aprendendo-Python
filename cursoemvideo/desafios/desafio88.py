from random import randint
from time import sleep
lista = list()
jogos = list()


quant = int(input('Quantos jogos quer fazer?: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1
print(jogos)
#for i, l in enumerate(jogos):
 #   print(f'Jogo {i + 1}: {l}')
  #  sleep(1)