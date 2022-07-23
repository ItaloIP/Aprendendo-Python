n = int(input('Quanto de dinheiro você pretende investir?: '))
j = float(input('Quanto que vai ser a taxa de juros anual?: '))
t = int(input('Quantos anos você pretende deixar este dinheiro investindo?: '))
j1 = j / 100
inv =  n * (1 + j1)**t
l = inv - n
print('Dentre {} anos, você vai obter R${:.2f} de lucro, e ao total, R${:.2f}. Vale apena investir?'.format(t,l,inv))
