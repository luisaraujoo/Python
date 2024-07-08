lista = []

while len(lista) < 5:
    valor = int(input(f'Adicione um numero para sua lista {len(lista) + 1}/5: '))
    lista.append(valor)

maiorvalor = max(lista)
menorvalor = min(lista)

print(f'O maior valor dessa lista se encontra na posição {lista.index(maiorvalor)}, ja o menor valor se en contra'
      f' na posição {lista.index(menorvalor)}')
