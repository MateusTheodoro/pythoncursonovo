frase = 'Hoje é Quarta-Feira'

contador = 0
nova_string = ''

while contador < len(frase):
    nova_string = nova_string + f'*{frase[contador]}'
    contador += 1
print(nova_string)