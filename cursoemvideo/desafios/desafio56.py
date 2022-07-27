idade = 0
media = 0
maiorhomem = 0
nomevelho = ''
totmulher20 = 0
for pessoa in range(1, 5):
    print('---{}Pessoa---'.format(pessoa))
    nome = str(input('Nome: '))
    id = int(input('Idade: '))
    s = str(input('Sexo: F ou M: ')).lower()
    
    idade += id
    
    if pessoa == 1 and s =='m':
        maiorhomem = id
        nomevelho = nome 
    
    if s == 'm' and id > maiorhomem:
        maiorhomem = id
        nomevelho = nome
    
    if s in 'f' and id < 20:
        totmulher20 += 1

media = idade / 4
print('A média do grupo é de {} anos.'.format(media))
print('O homem mais velho é o {} com {} anos.'.format(nome,idade))
print('Há {} mulher(es) com menos de 20 anos.'.format(totmulher20))
