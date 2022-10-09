try:
    a = int(input('>'))
    b = int(input('>>'))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um erro!')
except ZeroDivisionError:
    print('Não dá para dividir por zero.')
except KeyboardInterrupt:
    print('Sem entrada de teclado')
else:
    print(f'Resultado é {r}')
finally:
    print('Volte sempre!')
