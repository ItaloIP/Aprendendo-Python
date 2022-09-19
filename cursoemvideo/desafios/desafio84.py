lista = []
dados = []
num = 0
pesadas = []
leves = []
while True:
    name = str(input('Digite o nome da pessoa: ')).strip().capitalize()
    dados.append(name)
    peso = float(input(f'Qual o peso do {dados[0]}: '))
    dados.append(peso)

    if peso > 100:
        pesadas.append(dados[num:0])
    else:
        leves.append(dados[num:0])

    num += 1
    lista.append(dados[:])
    dados.clear()
    choice = str(input('Quer adicionar mais pessoas?: [S/N]  ')).strip().upper()
    if choice == 'N':
        break


print(f'Foram cadastradas {num} pessoas.')
print(f'As pessoas mais pesadas são: {pesadas}')
print(f'As pessoas mais leves são: {leves}')
