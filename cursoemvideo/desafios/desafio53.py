frase = str(input('Digite uma frase: ')).lower().strip().replace(' ', '')
n = len(frase)
for c in range(0,n,-n):
    if frase == frase:
        print('Está frase é um PALÍNDROMO')
