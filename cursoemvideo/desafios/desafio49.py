t = int(input('Digite um número que você quer saber da tabuada: '))
for c in range(1,11):
    print('{} x {:2} = {:2}'.format(t, c, t*c))
