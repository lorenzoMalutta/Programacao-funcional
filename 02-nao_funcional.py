def soma(lista):
    soma_valor = 0
    for valor in lista:
        soma_valor += valor
    return soma_valor


def dobro(lista):
    for i in lista:
        print(i*2)


def media(lista, tam):
    soma_valor = 0
    for valor in lista:
        soma_valor += valor
    return soma_valor / tam


L = [1, 2, 3, 4, 5]
tama = len(L)

print(f'A soma dos valores {soma(L)}')
print('O dobro dos valores: ')
dobro(L)
print(f'A media dos valores {media(L, tama)}')