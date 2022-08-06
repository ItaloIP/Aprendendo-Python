#Se o nome da cidade há SANTO
c = str(input('Que cidade você nasceu?: ')).strip().title()
print(c[:5].upper() == 'SANTO')
