def contador(*núm):
    # for valor in núm:
    #     print(f'{valor} ', end='')
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números')


contador(2, 1, 4)
contador(5)