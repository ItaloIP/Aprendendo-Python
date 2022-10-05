def Calcular(larg, comprimento):
    s = larg * comprimento
    print(f'O comprimento da área {larg}x{comprimento} é {s}m²')


#programa principal
c = float(input('Largura: '))
l = float(input('Comprimento'))
Calcular(c, l)
