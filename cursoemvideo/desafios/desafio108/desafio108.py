from moeda import moeda,aumentar,dob,met

money = float(input('Digite um valor: R$'))
print('-='*20)
print(f'\n10% de aumento de {moeda(money)} é {moeda(aumentar(money, 10))}')
print(f'\nO dobro de {moeda(money)} é {moeda(dob(money))}')
print(f'\nA metade de {moeda(money)} é {moeda(met(money))}')
