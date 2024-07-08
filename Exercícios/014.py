lista = []

while len(lista) < 6:
    valor = int(input(f'adicione um valor par para sua lista {len(lista) + 1}/6: '))
    if valor % 2 != 0:
        print('esse numero nao é par')
    else:
        lista.append(valor)

lista.reverse()

print(f'a lista de pares em modo reverso é {lista}')
