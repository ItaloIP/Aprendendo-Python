import random
import time

chances = 0
robo = int(random.randint(0,10))
print('ROBO: Estou pensando em um número entre 0 à 10... Qual você acha que é?')


n = int(input('Digite o número que vocÊ acha que o rob está pensando!: '))
while n != robo:
    if robo != n:
        chances += 1
    n = int(input('Errou!! Tente novamente!: '))


print('Parabéns!! Você acertou! Foram necessárias {} chances!'.format(chances + 1))
print('FIM!')
