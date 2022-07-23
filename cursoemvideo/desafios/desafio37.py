print('=-'*20)
print('\033[0;34;41mConversor\033[m')
print('=-'*20)

num = int(input('Digite um número inteiro'))
choice = int(input('''Você deseja converter 

( 1 ) Binário
( 2 ) Octal                    
( 3 ) Hexadecimal 
escolha: '''))


if choice == 1:
    print('A conversão do número {} para Binário é {}.'.format(num,bin(num)[2:]))
elif choice == 2:
    print('A conversão do número {} para Octal é {}.'.format(num,oct(num)[2:]))
elif choice == 3:
    print('A conversão do número {} para Hexadecimal é {}.'.format(num,hex(num)[2:]))
else:
    print('A opção escolhida não existe.')
