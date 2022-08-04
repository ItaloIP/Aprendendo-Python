n = int(input('Quantos termos você quer ver?'))
f1 = 0
f2 = 1
f3 = f1 + f2

print('{} > {}'.format(f1,f2), end='')
cont = 3
while cont <= n:
    f3 = f1 + f2
    print(' > {}'.format(f3), end='')
    f1 = f2 
    f2 = f3
    cont += 1 

print(' > Fim')
