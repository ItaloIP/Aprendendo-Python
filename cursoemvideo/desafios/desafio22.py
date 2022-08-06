#Manipulando as strings
name = str(input('Digite um nome: ')).strip()
m1 = name.upper()  #nome em maiúsculo
print('O nome em maiúsculo fica {}'.format(m1))

m2 = name.lower()   #Nome minúsculo
print('O nome em minúsculo fica {}.'.format(m2))

#m3 = len(name.replace(' ',''))
print('O nome têm a quantidade de caracteries {}.'.format(len(name) - name.count(' ')))   #contagem de caractéries

separa = name.split()

print('O primeiro nome têm de caractéries {}.'.format(len(separa[0])))      #contagem de caractéries (nome)                              
