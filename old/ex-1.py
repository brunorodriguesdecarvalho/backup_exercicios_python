a =input()
b, n = a.split()
b = int(b)
n =int(n)
while b!=0 or n!=0:

    r = input().split()
    for i in range(len(r)):
        r[i] = (int) (r[i])
    dcv  = []

    for i in range(n):
        Devedor ,Crededor, Valor = input().split()
        dcv.append([int (Devedor) ,int(Crededor), int(Valor)])
        r[int(Crededor)-1] +=  int(Valor)

    problem = False
    for i in range(n):
        if r[dcv[i][1]-1]  < dcv[i][2]:
            problem = True
     if problem:
        print("N")
    else:
        print("S")
    a =input()
    b, n = a.split()
    b = int(b)
    n =int(n)
