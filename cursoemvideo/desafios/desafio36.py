from time import sleep

#Boas Vindas
print('-='*21)
print('\033[0;31;47mOlá, bem vindo ao centro de empréstimo do Banco Galaia!\033[m')
print('-='*21)

#Info
house = float(input('Qual é o valor da casa?: '))
pay = float(input('Quanto que vocÊ recebe por mês?: '))
year = int(input('Pretende pagar em quantos anos o empréstimo?: '))

#'Carregamento'
print('Analisando...')
sleep(3)

#Contas
valor = house / year
valor1 = valor / 12
salario = pay * 0.3

print('Uma casa de R${:.2f} que o senhor(a) escolheu pagar em {} anos, a prestação será de R${:.2f} por mês.'.format(house,year,valor1))

if valor1 >  salario: #Empréstimo Negado
    print('\033[0;31;30mEMPRÉSTIMO NEGADO!\033[m ')
    print('Infelizmente o seu salário não permitira este empréstimo')
else: #Empréstimo Aprovado
    print('\033[0;34;30mEMPRÉSTIMO APROVADO!\033[m')

print('Tenha um bom dia!')
