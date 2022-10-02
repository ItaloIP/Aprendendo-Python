from math import sqrt

print('-'*25)
print('\033[0;32;45mEquação do 2° Grau\033[m')
print('-'*25)

a = int(input('Digite o valor do A: '))
b = int(input('Digite o valor do B: '))
c = int(input('Digite o valor do C: '))

delta = b**2 - 4 * (a * c)
print('=-='*15)
print(delta)
print('=-='*15)

menos = (-(b) - (sqrt(delta))) / (2 * a)
mais = (-(b) + (sqrt(delta))) / (2 * a)

print('=-='*15)
print(f'X1 = {mais:.2f}')
print(f'X2 = {menos:.2f}')
print('=-='*15)
