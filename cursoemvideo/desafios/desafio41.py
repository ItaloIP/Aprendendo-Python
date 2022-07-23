from datetime import date
ano = date.today().year

print('-=' * 17)
print('\033[0;36;40mSua Categoria de NADADOR!\033[m') #Boas Vindas
print('-=' * 17)

nano = int(input('Em que ano você nasceu?'))
idade = ano - nano

print('Você têm {} anos.'.format(idade))

if idade <= 9:
    print('Classificação: Mirim')

elif 9 >= idade < 14:
    print('Classificação: Infantil')

elif 14 >= idade < 19:
    print('Classificação: Junior')

elif 19 >= idade < 25:
    print('Classificação: Sênior')
elif idade >= 25:
    print('Classificação: MASTER')
