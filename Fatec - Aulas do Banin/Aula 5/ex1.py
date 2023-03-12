P = int(input("Digite o primeiro termo:"))
R = int(input('Digite a razão:'))
Q = int(input('Digite a quantidade de termos:'))
Cont = 0
while Cont < Q:
    print(P)
    P = P + R
    Cont += 1
