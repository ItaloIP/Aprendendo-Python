lista = []
dado = []
maior = menor = num = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if num == 0:
        menor = maior = dado[num:1]
    else:
        if maior < dado[num:1]:
            maior = dado[num:1]
        if menor > dado[num:1]:
            menor = dado[num:1]
    num += 1 
    lista.append(dado[:])
    dado.clear()
    choice = str(input('Quer adicionar mais pessoas?: [S/N]  ')).strip().upper()
    if choice == 'N':
        break

print(maior,menor)
'''
for c in lista:
    if c[1] == maior:
        print('ok')
    if c[1] == menor:
        print('ok')
'''

'''
print('-='*20)

print(f'Foram cadastradas {num} pessoas.')
print(f'O maior peso foi de {} e as pessoas mais pesadas são: {pesadas}')
print(f'O menor peso foi de {} e as pessoas mais leves são: {leves}')
'''