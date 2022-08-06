#ano bissexto
from datetime import date
year = int(input('Que ano você quer saber se é bissexto? (caso queira saber o ano da máquina, digite "0".: '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:    #Se o resto do ano por 4 for 0 e se o resto do ano por 100 (ou 400) for 0 é BISSEXTO
    print('O ano {} é BISSEXTO!'.format(year))
else:
    print('O ano {} é normal.'.format(year))
