sexo = str(input('Digite o seu sexo (M / F): ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Este sexo não existe! Digite um sexo válido (M / F): ')).upper().strip()[0]
print('Sexo {} registrado.'.format(sexo))
 