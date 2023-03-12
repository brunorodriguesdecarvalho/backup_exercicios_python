positivo = 0
negativo = 0
valor = 1
while valor != 0:
    if valor < 0:
        negativo += valor
    elif valor == 0:
        quit
    else:
        positivo += valor
    print('Total dos positivos: {}'.format(positivo))
    print('Total dos negativos: {}'.format(negativo))
    valor = int(input('Digite um valor inteiro para totalizar: '))

    
