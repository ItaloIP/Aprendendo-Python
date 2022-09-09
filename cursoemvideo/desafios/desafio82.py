numbers = list()
while True:
    numbers.append(int(input('Digite um valor: ')))
    choice = str(input('Quer continuar?[S/N]:  ')).strip().upper()
    print('-='*15)
    if choice == 'N':
        break
print(f'A lista de números que você digitou foi: {numbers}')


par = list()
impar = list()
for n in numbers:
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)

print(f'Números pares: {par}')
print(f'Números ímpares: {impar}')
