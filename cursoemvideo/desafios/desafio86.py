matriz1 = []
dados = []

#-----------------#

for c in range(0,9):
    dados.append(int(input(f'Digite um valor para:' )))
    matriz1.append(dados[:])
    dados.clear()

print()