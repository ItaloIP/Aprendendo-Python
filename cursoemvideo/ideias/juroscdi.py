n = float(input('Quanto de dinheiro você pretende investir?: '))
cdi = float(input('Quanto que está proposto o CDI?: %'))
a = int(input('Pretende deixar quantos anos investindo?: '))

#mude para o DIA do CDI que está realizando o processo
dia = 13.65 

cd = (((cdi * dia) / 100) / 100) + 1
r = n * (cd ** a)
r1 = r - n
print(f'Você obterá R${r1:.2f} de lucro e ao todo, terá R${r:.2f}')
