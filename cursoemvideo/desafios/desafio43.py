import math
print('=-' * 15)
print('\033[0;33;40mVocê está sobre o peso? Vamos descobrir!!\033[m')
print('=-' * 15)

peso = float(input('Qual o seu PESO? (em KG): '))
altura = float(input('E a sua altura? (em metros): '))
calc = peso / (altura ** 2)

print('O seu IMC é de {:.2f}'.format(calc))

if calc <= 18.5:
    print('Você está ABAIXO DO PESO!!')
elif calc <= 25.0:
    print('Você está no PESO IDEAL!')
elif calc <= 30.0:
    print('Você está SOBREPESO')
elif calc <= 40:
    print('Vocé está na OBESIDADE!!!')
else:
    print('VOCÊ ESTÁ COM OBESIDADE MÓRBIDA!!!')
