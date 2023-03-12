valor = int(input("Digite um número com cinco digitos: "))
if valor < 10000 or valor > 99999:
    print("O valor é inválido")
    while valor < 10000 or valor > 99999:
        valor = int(input("Digite um número com cinco digitos: "))
        if valor < 10000 or valor > 99999:
            print("Valor inválido")
        else:
            digito1 = (valor//10000)
            resto1 = (valor % (digito1*10000))
            digito2 = resto1//1000
            resto2 = resto1 - (digito2 * 1000)
            digito3 = resto2//100
            resto3 = resto2 - (digito3 * 100)
            digito4 = resto3//10
            resto4 = resto3 - (digito4*10)
            digito5 = resto4//1
            peso1 = digito1 * 6
            peso2 = digito2 * 5
            peso3 = digito3 * 4
            peso4 = digito4 * 3
            peso5 = digito5 * 2
            dv = (peso1 + peso2 + peso3 + peso4 + peso5)%7
            print("{}{}{}{}{}-{}".format(digito1, digito2, digito3, digito4,digito5,dv))
