nome = 'Mateus'
altura = 1.80
peso = 95
imc = peso / (altura * altura)

imc_formatado = f'{imc:.2f}'

print(nome + ', voce tem ' + str(altura) + ' de altura,')
print('pesa ' + str(peso) + ' quilos e seu IMC eh: ')
print(imc_formatado)