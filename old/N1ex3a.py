entrada_quantidade  = 1
entrada_valor = 1
valor_total = 0
qtd_vendas = 0

while entrada_quantidade != 0:
    entrada_quantidade = int(input("Digite a quantidade:"))
    if entrada_quantidade == 0 :
        print("fim")
        break  
    entrada_valor = float(input("Digite um valor:"))
    valor_total = (entrada_quantidade*entrada_valor)
    qtd_vendas += 1
    print(valor_total)
    print("Quantidade de vendas:", qtd_vendas)
        
    
            

        


