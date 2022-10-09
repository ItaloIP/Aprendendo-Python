from moeda import aumentar, dob, met

money = float(input('Digite um valor: R$'))
print(f'\n10% de aumento de R${money} é R${aumentar(money, 10)}')
print(f'\nO dobro de R${money} é R${dob(money)}')
print(f'\nA metade de R${money} é R${met(money)}')
