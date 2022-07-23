word = str(input('Digite uma frase qualquer: ')).strip().lower()
print('A letra "A" aparece {} vezes.'.format(word.count('a')))
print('A letra "A" aparece pela primeira no {} caractere.'.format(word.find('a')+1))
print('A ultima vez que aparece a letra "A" foi no {} caractere.'.format(word.rfind('a')+1))
