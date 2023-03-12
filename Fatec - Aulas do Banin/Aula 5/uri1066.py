i = 0
par = 0
imp = 0
pos = 0
neg = 0
for i in range(0,5):
    v = int(input())
    if (v%2) == 0:
        par += 1
    else:
        imp += 1
    if v > 0:
        pos += 1
    if v < 0:
        neg += 1
    i += 1
print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(imp))
print('{} valor(es) positivo(s)'.format(pos))
print('{} valor(es) negativo(s)'.format(neg))
