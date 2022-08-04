n =  s = 0
while True:
    n = int(input('Digite um número'))
    if n == 999:
        break
    s += n
#print('Soma é {}'.format(s))
print(f'A soma vale {s}')
