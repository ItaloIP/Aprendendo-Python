matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = c3 = 0

# ------- #

for l in range(0, 3):
    for c in range(0,3):
        matriz[l][c] = (int(input(f'Digite o valor para [{l},{c}]: ')))

        # If matriz is pair, sum pair
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        
        # Total in col 3
        c3 += matriz[l][2]
        
print('-='*25)
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^4}]',end='')
    print()

# High in line 2
maior = max(matriz[1])

print('-='*25)
print(f'A soma dos valores pares é {par}')
print(f'Soma da coluna 3 é {c3}')
print(f'O maior número da linha 2 é {maior}')