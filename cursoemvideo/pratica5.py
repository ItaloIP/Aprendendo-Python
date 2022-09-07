valores = list()
'''valores.append(5)
valores.append(9)
valores.append(4)'''

for cont in range (0, 5):
    valores.append(int(input('Digite um número')))

for c, b in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {b}')
print('Cheguei no final da lista')
