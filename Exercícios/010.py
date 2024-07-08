lista = []

while len(lista) < 8:
    valor = int(input(f'adicione um elemento na sua lista {len(lista) + 1}/8: '))
    lista.append(valor)

x = lista[3]
y = lista[5]

soma = x + y

print(f'A soma dos elementos 3 e 5 da sua lista é {soma}')
