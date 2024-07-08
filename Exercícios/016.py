lista = []
listanegativa = []
listapositiva = []

while len(lista) < 10:
    valor = float(input(f'Digite um numero real para sua lista {len(lista) + 1}/10: '))
    lista.append(valor)
    if valor < 0:
        listapositiva.append(valor)
    else:
        listanegativa.append(valor)

print(f'\nA quantidade de numeros negativos na lista é {len(listapositiva)}\n')
print(f'A soma dos valores positivos dessa lista é {sum(listanegativa)}')
