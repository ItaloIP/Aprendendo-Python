total = cont = cont1000 = baratop = 0
baraton = ''
print('Mercado')

while True:
    name = str(input('Produto: ')).upper().capitalize()
    price = float(input('Preço: R$'))
    

    if price >= 1000:
        cont1000 += 1

    if cont == 1:
        baratop = price
        baraton = name
    else:
        if price < baratop:
            baratop = price
            baraton = name

    total += price
    cont += 1

    choice = str(input('Quer adicionar mais produtos? [S/N]:  ')).strip().upper()[0]
    
    

    if choice == 'N':
        break

    
print(f'O total dos {cont} produtos foi de R${total:.2f}')
print(f'Foram {cont1000} produtos que são acima de R$1000')
print(f'O produto mais barato é o {baraton} que custa R${baratop:.2f}')
