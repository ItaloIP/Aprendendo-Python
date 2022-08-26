from random import randint



um = randint(0,10)
dois = randint(0,10)
tres = randint(0,10)
quatro = randint(0,10)
cinco = randint(0,10)

tupla = (um,dois,tres,quatro,cinco)
print(tupla)



maior = menor = um

if um > maior:
    maior = um
elif dois > maior:
    maior = dois
elif tres > maior:
    maior = tres
elif quatro > maior:
    maior = quatro
elif cinco > maior:
    maior = cinco



if dois < menor:
    menor = dois
elif tres < menor:
    menor = tres
elif quatro < menor:
    menor = quatro
elif cinco < menor:
    menor = cinco

print(maior)
print(menor)
