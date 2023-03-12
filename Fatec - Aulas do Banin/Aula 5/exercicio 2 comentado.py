x = 1
while x != 0:
    x = int(input('Digite um valor x diferente de 0: '))
    print('O valor digitado foi: {}' .format(x))
    print('{} dividido por 2: {}'.format(x,x/2))
    print('Para saber se qualquer número é par, o resto da divisão por 2 tem que ser zero')
    print('O resto da divisão de {} por 2 é: {}'.format(x,x%2))
    if (x%2) == 0:
        print('{} é par'.format(x))
    else:
        print('{} é ímpar'.format(x))
        
