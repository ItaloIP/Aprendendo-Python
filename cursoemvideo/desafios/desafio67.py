while True:
    print('-='*13)
    n = int(input('Quer verificar a tabuada de qual número?: '))
    print('-='*13)
    if n >= 0:
        for t in range(1,11):
            print(f'{n:2} x {t:2} = {n*t:2}')
    else:
        print('Programa Finalizado!')
        break
