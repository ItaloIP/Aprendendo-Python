frase = str(input('Digite uma frase: ')).lower().strip()
n = frase.split()
junto = ''.join(n)
contrario = ''

for frase in range(len(junto) - 1, -1, -1):
    contrario += junto[frase]


if contrario == junto:
    print('Está frase é um palíndromo')
else:
    print('Está frase não e um palíndromo')
