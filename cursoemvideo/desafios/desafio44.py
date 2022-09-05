from time import sleep
print('\033[0;32;31mLojas Galaia\033[m')

valor = float(input('Valor em R$ da compra?: R$'))

escolha = int(input('''Você deseja pagar:
( 1 ) Á vista dinheho ou cheque (10% de desconto)
( 2 ) Á vista no cartão (5% de desconto)
( 3 ) 2x no cartão
( 4 ) 3x ou mais no cartão (20% de juros)
: '''))

if escolha == 1:
    pay = valor * 0.90
    print('Ao pagar a vista com dinheiro, será aplicado 10% de desconto, então valor total será de R${:.2f}'.format(pay))
elif escolha == 2:
    pay = valor * 0.95
    print('Ao pagar a vista com cartão, será aplicado o desconto de 5%. O novo valor será de R${:.2f}'.format(pay))
elif escolha == 3:
    pay = valor / 2
    print('O valor será de R${:.2f} em 2x sem JUROS.'.format(pay))
elif escolha == 4:
    div = int(input('Dividir em quantas vezes?: '))
    if div >= 3:
        pay = (valor + (valor * 0.20)) / div 
        print('Você escolheu pagar em {}x, terá um acréscimo de 20% de juros.'.format(div))
        print('Carregando...')
        sleep (2)
        print('Ao total, você pagará R${:.2f} em {}x'.format(pay,div))
    else:
        print('Você não pode dividir em {}x, apenas 3x pra cima!')
else:
    print('Opção inválida.')
