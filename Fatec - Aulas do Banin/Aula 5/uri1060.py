i = 0
positivos = 0
for i in range(0,6):
    valor = float(input())
    if valor > 0:
        positivos +=1
    i += 1
print('{} valores positivos'.format(positivos))
