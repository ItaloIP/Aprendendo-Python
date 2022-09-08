mais = 0
while True:
    numbers = [int(input('Digite qualquer número: '))]
    choice = str(input('Quer continuar ?[S/N]:  ')).strip().upper()
    if choice == 'S':
        mais += 1
    elif choice == 'N':
        break