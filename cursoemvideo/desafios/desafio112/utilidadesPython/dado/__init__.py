def ReadMoney(money):
    while True:
        ans = str(input(money))
        ans2 = ans
        ans = ans.strip().replace('.','').replace(',','')
        if ans.isnumeric() == False:
            print(f'\033[0;31;40mERRO! "{ans}" não é o valor adequado.\033[m')
        else:
            if ',' in ans2:
                return float(ans2.replace(',','.'))
            else:
                return float(ans2)
