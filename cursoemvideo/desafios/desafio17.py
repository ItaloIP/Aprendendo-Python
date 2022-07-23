#Matemático / Import
'''from math import pow, sqrt
a = float(input('Informe o Comprimento do cateto oposto: '))
b = float(input('E o cateto adjacente: '))
s1 = (a ** 2) + (b ** 2)
hipo = sqrt(s1)

print(hipo) '''

from math import hypot
co = float(input('Informe o comprimento do Cateto Oposto: '))
ca = float(input('Informe o comprimento do Cateto Adjacente: '))
hi = hypot(co, ca)
print('O cálculo da hipotenusa é {:.2f}.'.format(hi))
