#Número inteiro de um número decimal
from math import trunc
num = float(input('Digite um número quebrado: '))
s = trunc(num)
print('O número escolhido foi {} e ele inteiro é {}.'.format(num,s))
