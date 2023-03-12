d = [int(x) for x in input().split()]
r = [int(x) for x in input().split()]

#continue desenvolvendo a solucao

Ca = d[0] 
Ba = d[1]
Pa = d[2]

Cr = r[0] 
Br = r[1]
Pr = r[2]

S = 0

if(Cr > Ca):
    S+=(Cr - Ca)

if(Br > Ba):
    S+=(Br - Ba)

if(Pr > Pa):
    S+=(Pr - Pa)

print(S)
