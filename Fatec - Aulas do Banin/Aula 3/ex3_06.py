nome = input("Digite um nome:")
peso = float(input("Digite um peso:"))

if peso < 65:
    categoria = "Pena"
elif peso < 72:
    categoria = "Leve"
elif peso < 79:
    categoria = "Ligeiro"
elif peso < 86:
    categoria = "Meio Médio"
elif peso < 93:
    categoria = "Médio"
elif peso < 100:
    categoria = "Médio Pesado"
else:
    categoria = "Pesado"

print ("O Lutador {} pesa {} e se enquadra na categoria {}".format(nome, peso, categoria))
