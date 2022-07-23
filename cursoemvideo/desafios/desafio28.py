from random import randint
from time import sleep
number = int(randint(0,5))
print('Vamos brincar? Estou pensando em um número dentre 0 e 5, qual eu estou pensando?')
e = int(input())
print('PENSANDO...')
sleep(3)
if e == number:
    print('Você acertou! Parabéns!!')
else:
    print('Errou! O número que eu estava pensando era o {}.'.format(number))

