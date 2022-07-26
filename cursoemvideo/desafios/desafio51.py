num = int(input('Digite um número'))
pa = int(input('Digite a PA'))
d = num + (10 - 1) * pa
for c in range(num , d + pa, pa):
    print('{}'.format(c), end= ' ')
print('fim')
