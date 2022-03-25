def soma(L, i, n, count):
    """
    :param L: A lista que contem os valroes a serem somados
    :param i: O inicializador
    :param n: Tamanho da lista
    :param count: Determina o tamanho, parada da recursao e a soma.
    :return: count
    """
    if n <= i:
        return count

    count += L[i]

    count = soma(L, i + 1, n, count)

    return count

def dobro(count):
    return count+count

L = [1, 2, 3, 4, 5]
count = 0
n = len(L)
print(f'A soma dos valores: {soma(L, 0, n, count)}')

media = lambda x, y: y/x

print(f'Media aritmetica {media(n, soma(L, 0, n, count))}')

resultado = map(dobro, L)

print(resultado)

for resultados in resultado:
    print(resultados, end = " ")
