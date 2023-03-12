Lista = ""
FaturamentoTotal = 0
Salgado = 0
Cachorro = 0
Hamburguer = 0
XBurguer = 0
Refrigerante = 0
Cod = 0
preço = 0

while Cod <= 5:
    Cod = int(input("Informe o código do produto vendido: "))
    if Cod == 1:
        preço = preço + 4
        Salgado = Salgado + 1
    elif Cod == 2:
        preço =  preço + 6
        Cachorro = Cachorro + 1
    elif Cod == 3:
        preço =  preço + 8
        Hamburguer = Hamburguer + 1
    elif Cod == 4:
        preço =  preço + 10
        XBurguer = XBurguer + 1
    elif Cod == 5:
        preço =  preço + 4.5
        Refrigerante = Refrigerante + 1
    FaturamentoTotal = preço
    if Cod >= 6:
        Q = Salgado + Cachorro + Hamburguer + XBurguer + Refrigerante
        print("Total de produtos vendidos: ", Q)
        print("Total de Vendas: R$ %.2f"%FaturamentoTotal)
        print("Quantidades por tipo de produto = Salgado:{}unidades - Cachorro-quente:{} unidades - Hamburguer:{} unidades - X-Burguer:{} unidades - Refrigerante:{} unidades" .format(Salgado,Cachorro, Hamburguer,XBurguer,Refrigerante))
