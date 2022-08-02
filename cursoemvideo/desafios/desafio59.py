from time import sleep
change = 0

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite o segundo valor: '))

while change != 5:
    print('=='*25)
    change = int(input('''O que você quer fazer com estes números?
    ( 1 ) soma
    ( 2 ) multiplicar
    ( 3 ) qual o maior?
    ( 4 ) escolher novos números
    ( 5 ) sair do programa
    escolha: '''))
    print('=='*25)

    sleep(0.8)


    if change == 1:
        soma = n1 + n2
        print('A soma entre {} e {} resulta em {}'.format(n1,n2,soma))
    
    elif change == 2:
        multi = n1 * n2
        print('A multiplicação entre {} e {} resulta em {}'.format(n1,n2,multi))

    elif change == 3:
        if n1 > n2:
            print('O maior número é o {}.'.format(n1))
        else:
            print('O maior número é o {}'.format(n2))
    
    elif change == 4:
        print('Digite outros números')
        sleep(1)
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite o seugndo valor: '))

    elif change == 5:
        print('Você escolheu sair.')
        sleep(0.7)
        print('Adeus!')
    else:
        print('Escolha inválida. Escolha novamente...')



    sleep(1.2)