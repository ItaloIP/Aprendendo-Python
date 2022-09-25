lista = [[],[]]
dados = list()
for c in range(1,8):
    dados.append(int(input(f'Digite o {c}^o número: ')))
    if (dados[0] % 2) == 0:
        lista[0].append(dados[:])
    else:
        lista[1].append(dados[:])
    dados.clear()
lista[0].sort()
lista[1].sort()
print(f'Os números pares foram: {lista[0]}')
print(f'Os números ímpares foram: {lista[1]}')
