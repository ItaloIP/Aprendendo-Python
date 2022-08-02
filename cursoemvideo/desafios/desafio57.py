sexo = str(input('Digite o seu sexo (M / F): ')).upper().strip()
sexos = 'M' or 'F'
if sexo != sexos:
    while sexo != sexos:
        sexo = str(input('Este sexo não existe! Digite um sexo válido (M / F): ')).upper().strip()
print('Sexo {} registrado.'.format(sexo))
