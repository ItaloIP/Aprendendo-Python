lista = []
dado = []
maior = menor = 0

# ---- memory (don't touch!) ---- #

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]

    lista.append(dado[:])
    dado.clear()
    choice = str(input('Quer adicionar mais pessoas?: [S/N]  ')).strip().upper()
    if choice == 'N':
        break

print('-='*20)

print(f'Foram cadastradas {len(lista)} pessoas.')
print(f'O maior peso foi de {maior} e as pessoas mais pesadas são: ', end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]},', end='')

print(f'\nO menor peso foi de {menor} e as pessoas mais leves são: ', end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]},', end='')
