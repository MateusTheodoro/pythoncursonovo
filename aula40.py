while True:
    numero1 = input('Digite o 1º número: ')
    numero2 = input('Digite o 2º número: ')
    operador = input('Digite o operador (+ - / *): ')

    if numero1.isdigit() and numero2.isdigit():
        
        nro1 = int(numero1)
        nro2 = int(numero2)

        if operador == '+':
            print(f'O resultado da soma é: {nro1 + nro2}')
            print('\n-- digite qualquer letra para sair --\n')
        
        elif operador == '-':
            print(f'O resultado da subtração é: {nro1 - nro2}')
            print('\n-- digite qualquer letra para sair --\n')

        elif operador == '*':
            print(f'O resultado da multiplicação é: {nro1 * nro2}')
            print('\n-- digite qualquer letra para sair --\n')

        elif operador == '/':
            print(f'O resultado da divisão é: {nro1 / nro2}')
            print('\n-- digite qualquer letra para sair --\n')
        
        else:
            break
    else:
        print('Digite apenas números:')
    