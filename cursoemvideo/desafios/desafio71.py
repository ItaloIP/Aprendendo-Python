from time import sleep

print('-='*20)
print('Banco Galatia')
print('-='*20)
sleep(1.0)
print()

money = int(input('Quer sacar quanto?:  '))
cin = vin = dez = um = 0

while True:
    if money >= 50:
        cin = money // 50
        money -= (cin*50)
        print(f'{cin} CÉDULAS DE R$50')
        if money == 0:
            break
        
    elif money >= 20:
        vin = money // 20
        money -= (vin*20)
        print(f'{vin} CÉDULAS DE R$20')
        if money == 0:
            break

    elif money >= 10:
        dez = money // 10
        money -= (dez*10)
        print(f'{dez} CÉDULAS DE R$10')
        if money == 0:
            break

    elif money >= 1:
        um = money // 1
        money -= (um*1)
        print(f'{um} CÉDULAS DE R$1')
        if money == 0:
            break

print('Volte sempre!')
