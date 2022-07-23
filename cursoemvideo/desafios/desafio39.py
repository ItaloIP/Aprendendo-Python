from datetime import date
from time import sleep

print('-=' * 17)
print('\033[0;36;40mVai servir ao exército? Descubra!\033[m') #Boas Vindas
print('-=' * 17)

sexo = int(input('''Qual o seu SEXO?:
( 1 ) Masculino
( 2 ) Feminino
: '''))

if sexo == 2:
    print('Não é obrigatório o seu alistamento')

elif sexo == 1:

    age = int(input('Em que ano você nasceu?: '))
    year = date.today().year  #Ano Atual
    idade = year - age

    print('Analisando...')
    sleep(2)

    if idade < 18:
        print('Ainda não está na hora! Falta(m) {} ano(s) para você se alistar!'.format(18 - idade))        #Jovem
    elif idade == 18:
        print('Está na hora de se alistar! Se apresente à um quartel mais proxímo a você!')     #Agora
    else:
        print('Já se passou do tempo de você se alistar! Faz mais de {} ano(s)!'.format(idade - 18))        #Tarde

else:
    print('Opção Inválida!')
