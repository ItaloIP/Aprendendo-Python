from math import sqrt

print('-'*25)
print('\033[0;32;45mEquação do Segundo Grau\033[m')
print('-'*25)

a = int(input('Digite o valor do A: '))
b = int(input('Digite o valor do B: '))
c = int(input('Digite o valor do C: '))

delta = b**2 - 4 * (a * c)
print(delta)

menos = (-(b) - (sqrt(delta))) / (2 * a)
mais = (-(b) + (sqrt(delta))) / (2 * a)

print('=-='*15)
print('X1 = {:.2f}'.format(mais))
print('X2 = {:.2f}'.format(menos))
print('=-='*15)
