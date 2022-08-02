from time import sleep
c = 0

num = int(input('Digite um número inteiro: '))
pa = int(input('Digite a razão aritmética: '))
d = num + (10 - 1) * pa
while not num > d:
    num = num + pa
    print(num, end=' > ')
    
print('FIM!')
