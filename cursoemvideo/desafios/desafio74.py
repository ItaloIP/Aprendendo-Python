from random import randint



um = randint(0,5)
dois = randint(0,5)
tres = randint(0,5)
quatro = randint(0,5)
cinco = randint(0,5)

tupla = (um,dois,tres,quatro,cinco)
print(tupla)

maior = um

menor = um

#arrumar o maior


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
