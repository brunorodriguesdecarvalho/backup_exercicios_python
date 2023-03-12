entrada = int(input("digite o tempo em segundos:"))

segundo = 1
minuto = 60 * 1
hora = 60*60
dia = 24*60*60

print(entrada//dia,"dia(s)")
resto = entrada % dia
print(resto//hora,"hora(s)")
resto = entrada % hora
print(resto//minuto,"minuto(s)")
resto = entrada % minuto
print(resto,"segundo(s)")
              
              
