P = float(input("Digite o primeiro termo:"))
R = float(input('Digite a razão:'))
Q = float(input('Digite a quantidade de termos:'))
Cont = 0
while Cont < Q:
    print(P)
    P = P * R
    Cont += 1
