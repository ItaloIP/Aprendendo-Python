from moeda import aumentar, dob, met, diminuir

money = float(input('Digite um valor: R$'))
print('-='*20)
print(f'10% de aumento de {money} é {aumentar(money, 10,False)}')
print(f'13% de reduzindo de {money} é {diminuir(money, 13,False)}')
print(f'O dobro de {money} é {dob(money,False)}')
print(f'A metade de {money} é {met(money,True)}')
