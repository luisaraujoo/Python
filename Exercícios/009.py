conjunto: list = []
novo_conjunto: list = []

while len(conjunto) < 10:
    valor = int(input(f'adicione um valor para sua lista {len(conjunto) + 1}/10: '))
    conjunto.append(valor)

for valor in conjunto:
    quadrado = valor ** 2
    novo_conjunto.append(quadrado)

print(f'O conjunto de numeros digitados é {conjunto}')
print(f'A lista do quadrado dos numeros desse conjunto são {novo_conjunto}')
