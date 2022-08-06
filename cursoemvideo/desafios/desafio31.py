km = float(input('Qual a distância em KM a sua viagem?: '))

if km > 200:    #Se os KM passar 200
    km1 = km * 0.45 #desconto de 0,05
    print('A sua viagem vai lhe custar R${:.2f}. R$0,05 de desconto em cada Km devido a longa estrada!'.format(km1))    
else:
    km2 = km * 0.50 #normal
    print('A sua viagem irá lhe custar R${:.2f}.'.format(km2))
