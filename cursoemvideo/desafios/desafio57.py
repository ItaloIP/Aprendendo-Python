from ctypes.wintypes import PUSHORT


sexo = str(input('Digite o seu sexo (M / F): ')).upper()
sexos = 'M' and 'F'
if sexo != sexos:
    while sexo != sexos:
        sexo = str(input('Este sexo não existe! Digite um sexo válido (M / F): ')).upper()
print('FIM')
