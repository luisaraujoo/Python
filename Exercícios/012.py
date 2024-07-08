lista = []

while len(lista) < 10:
    valor = int(input(f'digite um numero para acrescentar na sua lista {len(lista) + 1}/10: '))
    lista.append(valor)


print(f'O maior elemento da lista {lista} é {max(lista)}, ja o menor elemento é o {min(lista)}')