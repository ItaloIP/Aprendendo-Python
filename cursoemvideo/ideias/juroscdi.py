n = float(input('Quanto de dinheiro você pretende investir?: '))
cdi = float(input('Quanto que está proposto o CDI?: %'))
a = int(input('Pretende deixar quantos anos investindo?: '))

cd = (((cdi * 13.15) / 100) / 100) + 1
r = n * (cd ** a)
r1 = r - n
print('Você obterá R${:.2f} de lucro e ao todo, terá R${:.2f}'.format(r1, r))
