A=float(input("Digite o valor de A: "))
B=float(input("Digite o valor de B: "))
C=float(input("Digite o valor de C: "))
delta=(B**2)-(4*A*C)
print("O valor de delta é: ", delta)
baskharapositivo = ((-B) + (delta ** 0.5)) / (2 * A)
baskharanegativo = ((-B) - (delta ** 0.5)) / (2 * A)
if delta > 0:
    print("Caso 1: Delta maior que ZERO -> Duas raízes reais")
    print(baskharapositivo)
    print(baskharanegativo)
elif delta == 0:
    print("Caso 2: Delta igual a ZERO -> Apenas uma raíz real")
    print(baskharapositivo)
else:
    print("Caso 3: Delta menor que ZERO -> Não há raízes reais")
