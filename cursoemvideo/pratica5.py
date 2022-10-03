def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [7, 1, 5, 9 ]
dobra(valores)
print(valores)
