SALGADO = int(0)
CACHORRO = 0
HAMBURGUER = 0
XB = 0
REFRIGERANTE = 0
ITENS = 0
TOTAL = 0
preço = 0
Q = 0
CODIGO = 6

while CODIGO < 7:
	CODIGO = int(input("Digite o código do produto: "))
	if CODIGO == 1:
		SALGADO = SALGADO + 1
		preço = preço + 4.00
	if CODIGO == 2:
		CACHORRO = CACHORRO + 1
		preço = preço + 6
	if CODIGO == 3:
		HAMBURGUER = HAMBURGUER + 1
		preço = preço + 8
	if CODIGO == 4:
		XB = XB + 1
		preço = preço + 10
	if CODIGO == 5:
		REFRIGERANTE = REFRIGERANTE + 1
		preço = preço + 4.50
	if CODIGO == 8:
		Q = SALGADO + CACHORRO + HAMBURGUER + XB + REFRIGERANTE
		TOTAL = preço
print("O total de itens vendidos é igual a ", Q)
print("Total de vendas é: R$",TOTAL)
print("Quantidades por tipo de Produto: ", "1:", SALGADO, "unidades", "2:", CACHORRO, "unidades", "3:", HAMBURGUER, "unidades", "4:", XB, "unidades", "5:", REFRIGERANTE, "unidades")
