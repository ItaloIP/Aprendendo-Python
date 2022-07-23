print('-==-' * 6)
print('\033[0;35;46mComparador de Números\033[m')          #Boas Vindas
print('-==-' * 6)

n1 = int(input('Digite um valor Inteiro: '))
n2 = int(input('Digite o segundo valor Inteiro: '))


if n1 > n2:
    print('O PRIMEIRO número é maior')

elif n2 > n1:
    print('O SEGUNDO número é maior')

else:
    print('Os dois números são iguais')
