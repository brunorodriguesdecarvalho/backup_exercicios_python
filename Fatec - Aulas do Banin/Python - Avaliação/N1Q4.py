n = -1
nce = 0
ncq = 0
nv = 0
nd = 0
nota5 = 0
ndo = 0
while n == 3 or n == 1 or n <= 0:
    n = int(input("digite o valor: "))
if n % 2 != 0 :
    nota5 = 1
    n = n - 5
if n >= 100:
    nce = n//100
    n = n - (nce * 100)
if 50 <= n < 100:
    ncq = 1
    n = n - 50
if 20 <= n < 50:
    nv = n//20
    n = n - (nv * 20)
if 10 <= n < 20:
    nd = 1
    n = n - (nd*10)
if 0 < n < 10:
    ndo = n//2
print("{} x R$:100,00 + {} X R$:50,00 + {} X R$:20,00 +{} X R$:10,00 +{} X RS:5,00 + {} X R$:2,00".format(nce,ncq,nv,nd,nota5,ndo))
    
        
        

        
