lista = []
dado = []
maior = num = 0
menor = 999
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))

    num += 1 
    lista.append(dado[:])
    dado.clear()
    choice = str(input('Quer adicionar mais pessoas?: [S/N]  ')).strip().upper()
    if choice == 'N':
        break

print('-='*20)

print(f'Foram cadastradas {num} pessoas.')
print(f'O maior peso foi de {maior} e as pessoas mais pesadas são:', end='')
for p in lista:
    if p[1] >= maior:
        print(f'{p[0]},')

print(f'\nO menor peso foi de {menor} e as pessoas mais leves são:', end='')
for p in lista:
    if p[1] >= menor:
        print(f'{p[0]},')
