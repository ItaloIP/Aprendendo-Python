#Desconto de um produto
p = float(input('Digite um valor de um produto: '))
d = float(input('Quantos  de desconto você deseja neste produto? %'))

#etapa 1

r = p - (p * d / 100)

#final

print('O preço com {:.2f}% de desconto será de R${:.2f}, vale apena!!'.format(d, r))
