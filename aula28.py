nome = input('Digite o seu nome: ')
idade = input('Digite a idade: ')

if nome == '' or idade == '':
    print('Você precisa preencher os dois campos!')
else:
    print(f'Seu nome é: {nome}')

    print(f'Seu nome invertido é: {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome tem espaços')
    else:
        print('Seu nome não tem espaços')
    
    print(f'Seu nome tem: {len(nome)} letras')

    print(f'A primeira letra do seu nome é: {nome[0]}')

    print(f'A última letra do seu nome é: {nome[-1]}')
