number1 = int(input('Digite qualquer número: '))
number2 = int(input('Digite qualquer número: '))
number3 = int(input('Digite qualquer número: '))
number4 = int(input('Digite qualquer número: '))
pares = 0
tupla = (number1,number2,number3,number4)
tuplap = ''

'''if number1 % 2 == 0:
    tuplap += number1
    print(f'O {number1} é PAR!')
if number2 % 2 == 0:
    tuplap += number2
    print(f'O {number2} é PAR!')
if number3 % 2 == 0:
    tuplap += number3
    print(f'O {number3} é PAR!')
if number4 % 2 == 0:
    tuplap += number4
    print(f'O {number4} é PAR!')'''
print('-'*20)
print(f'Você digitou os valores {tupla}')
print('O número NOVE apareceu', tupla.count(9), 'vezes!')

if tupla.index(3) == 0:
    print('O valor TRÊS não foi encontrado')
else:
    print('O número TRÊS está na posição', tupla.index(3)+1)

print(f'Números pares: ')
