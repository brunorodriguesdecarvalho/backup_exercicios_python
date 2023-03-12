i=0
p=0
s=0
while i < 6:
    values=float(input())
    i += 1
    if values > 0:
        p += 1
        s += values
print('{} valores positivos'.format(p))
print('{:.1f}'.format(s/p))
