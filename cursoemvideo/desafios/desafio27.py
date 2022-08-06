name = str(input('Digite seu nome completo: ')).strip().capitalize()
sepa = name.split()
print('Opa, oi!, {}, prazer te conhecer!'.format(name)) 
print('Seu primeiro nome é {}.'.format(sepa[0])) #Primeiro nome da pessoa
print('Seu último nome é {}.'.format(sepa[len(sepa)-1])) #Último nome
