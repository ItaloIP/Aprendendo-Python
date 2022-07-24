s = 0
for c in range (0,501,3):
    n = int(c)
    num = n % 2
    if num == 1:
        s += n
print(s)