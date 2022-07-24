from datetime import date
year = date.today().year
for c in range(0,7):
    anonas = int(input('Em que ano nasceu?: '))
    age = year - anonas
    maior = 3
    if age >= 21:
