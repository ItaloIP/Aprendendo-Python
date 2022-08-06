soma18 = somah = somam = 0
cont = 1

print('Cadastramento')

while True:
    sexo = ' '
    print(f'Cadastrando a pessoa número {cont}')
    idade = int(input(f'Digite à IDADE: ')) 

    while sexo not in 'FM':
        sexo = str(input('Digite um SEXO [M ou F]: ')).strip().upper()[0]

    if idade >= 18:
        soma18 += 1

    cont += 1
    if sexo == 'M':
        somah += 1

    if sexo == 'F' and idade < 20:
        somam += 1
    print('')
    print('PESSOA CADASTRADA!')
    print('')
    yon = str(input('Quer continuar a cadastrar pessoas? [S/N]: ')).upper()[0].strip()
    
    while yon not in 'SN':
        yon = str(input('Quer continuar a cadastrar pessoas? [S/N]: ')).upper()[0].strip()

    if yon == 'N':
        break
        

      
print(f'Há {soma18} pessoas acima de 18 anos.')
print(f'Há {somah} homens neste cadastro.')
print(f'Há {somam} mulheres abaixo de 20 anos.')
