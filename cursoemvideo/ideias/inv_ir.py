from time import sleep

print('-='*15)
print('Calculadora de investimento')
print('-='*15)

sleep (1)


while True:
    print('--'*20)
    print('''Que tipo investimento você deseja fazer?
    ( 1 ) Lci
    ( 2 ) CDB 
    ( 0 ) sair
    ''')
    choice = int(input('Escolha:  '))

    if choice == 1:
        print('-='*15)
        print('Qual o valor de entrada?: ')
        money = float(input('R$'))

        print('Qual o juros ao ano?')
        juros = float(input('%'))
        juros = juros / 100 # Tranformando a porcentagem em decimal

        print('Qual o período que você pretende deixar?')
        temp = float(input())

        print('''Pretende adicionar dinheiro mensalmente?
        ( 1 ) Sim
        ( 2 ) Não''')
        choice2 = int(input())

        if choice2 == 1:
            print('Manutenção...')
            sleep(0.8)
            '''
            print('Pretende adicionar quanto por mês?')
            mensal = float(input('R$'))
            print('Calculando...')
            sleep(0.8)                                  #codar a porcentagem com o valor diferente em todos os meses
            t2 = 12 * temp
            resul = (money + (mensal*t2)) * ((1 + juros)*temp)
            lucro = resul - money 
            print('-='*10)
            print(f'Ao total, renderá R${lucro:.2f} e ao todo terá R${resul:.2f}')
            '''
        elif choice2 == 2:
            print('Calculando...')
            resul = money * ((1 + juros)*temp)
            lucro = resul - money
            sleep(0.8)
            print('-='*10)
            print(f'Ao total, renderá R${lucro:.2f} e ao todo terá R${resul:.2f}')



    elif choice == 2:
        print('Qual o valor da entrada?')
        money = float(input('R$ '))
        print('Juros anual?')
        juros = float(input())
        juros = juros / 100 #Juros em decimal    
        print('Pretende deixar quanto tempo?')
        temp = float(input())
        
        print('''Pretende adicionar dinheiro mensalmente?
        ( 1 ) Sim
        ( 2 ) Não''')
        choice2 = int(input())

        if choice2 == 1:
            print('Manutenção...')
            sleep(0.8)

        elif choice2 == 2:
            print('Calculando...')
            temp2 = temp * 365
            resul = money * ((1 + juros)*temp)
            lucro = resul - money

            if temp2 <= 180:
                ir = 0.225
            elif temp2 <= 360:
                ir = 0.20
            elif temp2 <= 720:
                ir = 0.175
            elif temp2 >= 721:
                ir = 0.15

            imposto = lucro * ir
            lucro = lucro - imposto
            resul = resul - imposto

            print(f'Devido o investimento no CDB, você pagou R${imposto:.2} de imposto, então seu lucro foi de R${lucro:.2f} e ao total é R${resul:.2f}')

            sleep(0.8)
            print('-='*10)
            print(f'')


    elif choice == 0:
        print('Programa encerrado, adeus!')
        break
