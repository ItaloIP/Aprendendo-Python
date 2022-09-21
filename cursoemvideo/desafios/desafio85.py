lista = []
par = []
impar = []

for c in range(1,8):
    lista.append(int(input(f'Digite o {c}^o número: ')))

for num in lista:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

par.sort()
impar.sort()

print(f'Os números pares foram: {par}')
print(f'Os números ímpares foram: {impar}')
