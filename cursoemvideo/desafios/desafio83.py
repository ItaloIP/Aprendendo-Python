pardireita = paresquerda = 0
expressão = list(str(input('Digite uma expressão: ')).strip())

#realiza a contagem dos parenteses
paresquerda = expressão.count('(')
pardireita = expressão.count(')')

#Caso os parênteses não estejam iguais, está INCORRETO 'else:'
if paresquerda == pardireita:
    print('A expressão está correta!')
else:
    print('\033[0;31;41mA expressão está incorreta! (Há um parênteses errado!)\033[m')
