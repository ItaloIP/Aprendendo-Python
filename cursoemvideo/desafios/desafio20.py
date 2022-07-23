from random import shuffle
g1 = input('O primeiro grupo?: ')
g2 = input('O segundo grupo?: ')
g3 = input('O terceiro grupo?: ')
g4 = input('O quarto grupo?: ')

lista = [g1,g2,g3,g4]

shuffle(lista)

print('A ordem será: ')
print(lista)
