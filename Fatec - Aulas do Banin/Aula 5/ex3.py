P = int(input("Digite o primeiro termo:"))
R = int(input('Digite a razão:'))
Q = int(input('Digite a quantidade de termos:'))
Cont = 0
S = 0
T = 1
while Cont < Q:
    print('Termo {} da PA: {}'.format(T, P))
    S = S + P
    P = P + R
    Cont += 1
    T += 1
print('somatória de todos os termos(S):{}'.format(S))
