
# ------- 01
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero_usuario = input('Digite um número inteiro: ')
# numero_inteiro = numero_usuario.isnumeric()

# if numero_inteiro:

#     numero_inteiro = int(numero_usuario)
#     if numero_inteiro % 2 == 0:
#         print('Seu número é par.')
#     else:
#         print('Seu nome é ímpar')
        
# else:
#     print('Você não digitou um número inteiro')

# --------------


# ------- 02
"""
# Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
# descrito, exiba a saudação apropriada. Ex. 
# Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
# """
# horario = input('Olá. Que horas são? ')
# horas = int(horario)

# if horas > 0 and horas <= 11:
#     print('Bom dia!!')

# elif horas > 11 and horas <= 17:
#     print('Boa tarde!!')

# elif horas > 17 and horas <= 23:
#     print('Boa noite!!')

# else:
#     print('Digita entre 0-23')

# --------------

# ------- 03
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite o seu nome: ')
contagem = len(nome)

if contagem <= 4:
    print('Seu nome é curto!')

elif contagem <= 6:
    print('Seu nome é normal!')

elif contagem > 6:
    print('Seu nome é muito grande!')

else:
    print('Deu errado')


# --------------

