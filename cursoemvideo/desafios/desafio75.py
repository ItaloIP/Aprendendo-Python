number1 = int(input('Digite qualquer número: '))
number2 = int(input('Digite qualquer número: '))
number3 = int(input('Digite qualquer número: '))
number4 = int(input('Digite qualquer número: '))
pares = 0
tupla = (number1,number2,number3,number4)
tuplap = ''


print('-'*20)
print(f'Você digitou os valores {tupla}')
print('O número NOVE apareceu', tupla.count(9), 'vezes!')

if tupla.index(3) == 0:
    print('O valor TRÊS não foi encontrado')
else:
    print('O número TRÊS está na posição', tupla.index(3)+1)

print(f'Números pares: ')
