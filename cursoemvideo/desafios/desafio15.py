#Cálculo do aluguel de carro
day = int(input('Quantos dias você ficou com o carro?: '))
km = float(input('Quantos KM você rodou?: '))

s = (day * 60) + (km * 0.15)

print('Você terá que pagar aproximadamente R${:.2f}.'.format(s))
