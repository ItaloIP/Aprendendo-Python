#Conversor de Moeda
m = float(input('Reais você têm?: R$ '))
money = m / 5.16
euro = m / 5.26
libra = 6.23
print('Você consegue comprar ${:.2f}, pouco, né?'.format(money))
print('Você consegue comprar EUR{:.2f}, de EURO'.format(euro))
print('Você consegue comprar £{:.2f} de libra'.format(libra))
