from random import randint
from time import sleep

chances = 0
robo = int(randint(0,10))
print('ROBO: Estou pensando em um número entre 0 à 10... Qual você acha que é?')
n = int(input('Digite o número que vocÊ acha que o robo está pensando!: '))
sleep(1)
while n != robo:
    if robo != n:
        chances += 1
    print('Errou! {}'.format('É menos!'if n > robo else 'É mais!'))
    n = int(input('Tente novamente!: '))


print('Parabéns!! Você acertou! Foram necessárias {} chances!'.format(chances + 1))
print('FIM!')
