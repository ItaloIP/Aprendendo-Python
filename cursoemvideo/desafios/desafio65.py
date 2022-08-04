s = 0
cont = 0
n = float(input('Digite um número: '))
c = str(input('Quer continuar?:[S/N]  ')).strip().upper()
cont += 1
s += n

while c != 'N':
    if c == 'S':
        n = float(input('Digite um número: '))
        c = str(input('Quer continuar?:[S/N]  ')).strip()[0].upper()
        cont += 1
        s += n

print('Foram ao total {} números e a média deles é de {:.2f}'.format(cont,s/cont))
