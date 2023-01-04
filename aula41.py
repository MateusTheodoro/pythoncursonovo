""" While / else """
frase = 'Qualquer valor.'

i = 0
while len(frase) > i:
    soletra = frase[i]

    if soletra == ' ':
        break

    print(soletra)
    i += 1
else:
    print('Ainda no While.')

print('Fora do While.')
