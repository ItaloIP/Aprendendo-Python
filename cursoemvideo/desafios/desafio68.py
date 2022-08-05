from time import sleep
from random import randint

cont = soma = 0

print('=-'*20)
print('\033[0;33;46mPar ou Ímpar?\033[m')  #Boas Vindas
print('=-'*20)

sleep(0.8)
print('=-'*30)
print('O objetivo é você jogar PAR ou IMPAR contra seu COMPUTADOR, se perder, o jogo finalizara!')
print('=-'*30)
sleep(0.8)

while True:
    n = int(input('Número: '))
    poi = str(input('Par ou Ímpar? [P/I]:  ')).upper().strip()[0]
    robo = randint(0,10)
    soma = robo + n
    
    if poi == 'P' and soma % 2 == 0:
        cont += 1
        print(f'Parabéns! Você ganhou a {cont} rodada!')
        sleep(0.5)
    elif poi == 'I' and soma % 2 == 1:
        cont += 1
        print(f'Parabéns! Você ganhou a {cont} rodada!')
        sleep(0.5)
    else: 
        print('TURURUUUU')
        break

print('--'*15)
sleep(0.9)
print(f'PERDEU! Você venceu {cont} vezes.')
print('--'*15)
