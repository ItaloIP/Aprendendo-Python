numbers = [int(input('Digite qualquer número: '))]
while True:
    choice = str(input('Quer continuar?[S/N]:  '))
    if choice == 'N':
        break
    elif choice == 'S':
        numbers = [int(input('Digite outro número: '))]
        
