from math import factorial
from time import sleep
n = int(input('Digite um número: '))
c = n
f = factorial(n)
print('Calculando {}!'.format(n))
sleep(0.5)
print('Calculando.'.format(n))
sleep(0.5)
print('Calculando..'.format(n))
sleep(0.5)
print('CALCULADO!'.format(n))

while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = {}'.format(f), end='')
    c -= 1
