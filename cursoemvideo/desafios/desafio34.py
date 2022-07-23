pay = float(input('Quanto que é o seu salário?: '))
if pay > 1250.00:
    mais = pay + (pay * 10 / 100)
else:
    mais = pay + (pay * 15 / 100)
print('Seu salário será de R${:.2f}'.format(mais))
