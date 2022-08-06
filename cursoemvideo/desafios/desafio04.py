#Descobrir cada coisa da string

name = input('Digite algo, pode ser qualquer coisa!')
print('O tipo primitivo deste valor é', type(name))
print('É um número?', name.isalnum())
print('É alfanumérico?'.format(name.isalpha()))
print('Está em minúsculo? {}' .format(name.islower()))
