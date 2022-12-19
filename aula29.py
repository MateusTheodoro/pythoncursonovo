numero = input('Digite um número para dobrar o valor: ')

try:
    numero = float(numero)
    print(f'O número é: {numero * 2}')
except:
    print('Digite um número!')
