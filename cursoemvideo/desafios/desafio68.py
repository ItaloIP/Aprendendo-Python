from time import sleep
from random import randint

cont = 0

print('=-'*20)
print('\033[0;33;46mPar ou Ímpar?\033[m')
print('=-'*20)

sleep(0.8)
print('=-'*20)
print('O objetivo é você jogar PAR ou IMPAR contra seu COMPUTADOR, se perder, o jogo finalizara!')
print('=-'*20)
sleep(0.8)

while True:
    n = int(input('Número: '))
    poi = str(input('Par ou Ímpar? [P/I]:  ')).upper().strip()[0]

    robo = randint(0,10)



print(f'PERDEU! Você venceu {cont} vezes.')
