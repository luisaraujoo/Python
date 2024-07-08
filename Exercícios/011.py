lista = []
contadordepares = 0

while len(lista) < 10:
    valor = int(input(f'digite um valor para a lista {len(lista) + 1}/10: '))
    lista.append(valor)

    if valor % 2 == 0:
        contadordepares = contadordepares + 1

if contadordepares > 0:
    print(f'A sua lista contem {contadordepares} numeros pares')
else:
    print('A sua lista nao contem numero pares')