lista = []

while len(lista) < 6:
    valor = int(input(f'Adicione um valor para sua lista {len(lista) + 1}/6: '))
    lista.append(valor)

lista.reverse()

print(f'a lista em modo reverso é {lista}')
