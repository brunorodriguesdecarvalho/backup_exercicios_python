entrada = int(input("digite um valor: "))
saldo = float'(0)
if (entrada%2 == 0):
    if entrada > 100:
        print("notas de 100: ",(entrada//100))
        saldo = (entrada%100)
    if saldo > 50:
        print("notas de 50: ",(saldo//50))
        saldo = (entrada%50)
    if saldo > 20:
        print("notas de 20: ",(saldo//20))
        saldo=(saldo%20)
    if saldo > 10:
        print("notas de 10: ",(saldo//10))
        saldo=(saldo%10)
    if saldo > 5:
        print("notas de 5: ",(saldo//5))
        saldo = (saldo%5)
    if saldo > 2:
        print("notas de 2: ",(saldo//2))
        print(saldo%2)
if (entrada%2 != 0):
    entrada -= 5
    if entrada > 100:
        print("notas de 100: ",(entrada//100))
        saldo = (entrada%100)
    if saldo > 50:
        print("notas de 50: ",(saldo//50))
        saldo = (saldo%50)
    if saldo > 20:
        print("notas de 20: ",(saldo//20))
        saldo=(saldo%20)
    if saldo > 10:
        print("notas de 10: ",(saldo//10))
        saldo=(saldo%10)
    if saldo > 2:
        print("notas de 2: ",(saldo//2))
        print(saldo%2)
        if saldo >= 5:
            print("notas de 5: ",(saldo//5))
            saldo = (saldo%5)
        
    
    



    
