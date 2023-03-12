lista = []
carros = 0
casas = 0
while(carros != 999):
    carros = int(input())
    if(carros != 999 and carros > 2):
        lista.append(carros-2)
        casas = casas + 1
resultado = sum(lista)*12.89
print("{0:4.2f}".format(resultado))
print(casas)
    