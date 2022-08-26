extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze' ,'Doze' ,'Treze' ,'Quatorze' ,'Quinze' ,'Dezesseis' ,'Dezessete' ,'Dezoito' ,'Dezenove' ,'Vinte')
while True:
    ler = int(input('Digite um número entre 0 à 20: '))
    if 0 <= ler <= 20:
        break
    print('tente novamente. ', end='')
print(extenso[ler])
