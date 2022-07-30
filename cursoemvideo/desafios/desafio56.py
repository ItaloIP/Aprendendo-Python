somaidade = 0
mediaidade = 0
maiorhomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('======{} Pessoa ========'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo F/M: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomevelho - nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade destas pessoas é de {} anos.'.format(mediaidade))
print('O homem mais velho se chama {} e tem {} anos.'.format(nomevelho,maiorhomem))
print('Ao todo, são {} mulher com menos de 20 anos.'.format(totmulher20))
