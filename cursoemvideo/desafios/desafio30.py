#Par ou Ímpar
number = int(input('Digite um número: '))
num = number % 2

if num == 0:    #Se o resto de NUM por 2 for 0
    print('O número {} é PAR!'.format(number))
else:
    print('O número {} é IMPAR!'.format(number))
    