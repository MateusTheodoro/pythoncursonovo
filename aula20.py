primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f"{primeiro_valor=} é maior do que {segundo_valor=}")

elif primeiro_valor < segundo_valor:
    print(f"{segundo_valor=} é maior do que {primeiro_valor=}")

else:
    print(f"{primeiro_valor=} é igual a {segundo_valor=}")