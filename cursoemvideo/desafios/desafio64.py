s = 0
c = 0
cont = 0
n = int(input('Digite um número: '))
s += n
while n != 999:
    n = int(input('Digite um número: '))
    cont += 1
    s += n
print('Você digitou {} números e ao todo a soma deles foram de {}.'.format(cont,s - 999))
