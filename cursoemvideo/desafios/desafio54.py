from datetime import date
year = date.today().year
maior = 0
menor = 0
for pessoa in range (1,8):
    nasc = int(input('Em que ano a {} pessoa nasceu'.format(pessoa)))
    idade = year - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Temos {} pessoas maiores de idade.'.format(maior))
print('Temos {} pessoas menores de idade.'.format(menor))
