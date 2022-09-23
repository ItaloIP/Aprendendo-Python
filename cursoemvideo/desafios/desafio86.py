matriz = []
dados = []
num = 0
numh = 0

#-----------------#

for c in range(0,9):
    dados.append(int(input(f'Digite um valor para: {numh, num}: ')))
    num += 1
    if num == 3:
        num = 0
        numh += 1

    if numh == 0:
        matriz.append(dados[:])
    elif numh == 1:
        matriz.append(dados[:])
    else:
        matriz.append(dados[:])

print(matriz[0])
print(matriz[0:2])
print(matriz[0:3])
