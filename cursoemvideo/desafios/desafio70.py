total = cont = cont1000 = 0
barato = ' '
print('Mercado')

while True:
    name = str(input('Produto: '))
    price = float(input('Preço: '))

    if price >= 1000:
        cont1000 += 1


    barato = price
    if price 



    total += price
    cont += 1

    choice = str(input('Quer adicionar mais produtos? [S/N]:  ')).strip().upper()[0]

    if choice == 'N':
        break

print(f'O total dos {cont} produtos foi de R${total}')
print(f'Foram {cont1000} produtos que são acima de R$1000')
