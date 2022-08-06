#Verificação
word = str(input('Digite uma frase qualquer: ')).strip().lower()
print('A letra "A" aparece {} vezes.'.format(word.count('a'))) #Contagem da letra A
print('A letra "A" aparece pela primeira no {} caractere.'.format(word.find('a')+1)) #Onde aparece a letra A
print('A ultima vez que aparece a letra "A" foi no {} caractere.'.format(word.rfind('a')+1)) #Ultimá aparição da letra A
