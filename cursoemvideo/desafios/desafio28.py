from random import randint
from time import sleep  #fútil

number = int(randint(0,5))
print('Vamos brincar? Vou pensar em um número dentre 0 e 5, ')

e = int(input('Qual número o seu computador vai pensar?: '))    #palpite do usuário
print('PENSANDO...')

sleep(3)
if e == number: #Se for o mesmo número que o robo estiver 'pensando'
    print('Você acertou! Parabéns!!')
else:
    print('Errou! O número que eu estava pensando era o {}.'.format(number))

