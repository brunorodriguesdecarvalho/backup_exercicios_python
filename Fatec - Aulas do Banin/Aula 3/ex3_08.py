A=float(input("Digite o tamanho do primeiro lado: "))
B=float(input("Digite o tamanho do segundo lado: "))
C=float(input("Digite o tamanho do terceiro lado: "))

##para três números formarem um triângulo, a soma dos dois lados menores deve ser maior que o lado maior
##descobrindo qual é o lado maior
if A > B and A > C:
    maiorlado = A
    ladosmenores = B + C
elif B > C and B > A:
    maiorlado = B
    ladosmenores = A + C
else:
    maiorlado = C
    ladosmenores = B + A

print("O maior lado mede {:.2f}".format(maiorlado))
print("A soma dos menores lado mede {:.2f}".format(ladosmenores))

if ladosmenores > maiorlado:
    print("Portanto, este é um triângulo. A soma dos lados menores é maior que o maior lado.")
else:
    print("Portanto, com base nas medidas informadas, não é possível formar um triângulo.")

if A == B and B==C:
    print("Esse triângulo é equilátero, pois os três lados possuem o mesmo tamanho.")
elif not A == B and not B==C:
    print("Esse triângulo é escaleno, pois os três lados possuem medidas diferentes.")
else:
    print("Esse triângulo é isóceles, pois dois dos três lados desse triângulo possuem medidas iguais.")