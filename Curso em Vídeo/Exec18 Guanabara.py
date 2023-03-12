from math import sin, cos, tan, radians
anguloqualquer = float(input("Digite um angulo qualquer:"))
print("Este é o seno do ângulo {}: {:.2f}".format(anguloqualquer,sin(radians(anguloqualquer))))
print("Este é o cosseno do ângulo {}: {:.2f}".format(anguloqualquer,cos(radians(anguloqualquer))))
print("Este é o valor da tangente do ângulo {}: {:.2f}".format(anguloqualquer,tan(radians(anguloqualquer))))