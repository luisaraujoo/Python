"""3. Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele
possui."""

lista = []
contador_pares = 0

while len(lista) < 10:
    valor = int(input(f'informe um valor {len(lista) + 1}/10: '))
    lista.append(valor)

    if valor % 2 == 0:
        contador_pares = contador_pares + 1


if contador_pares > 0:
    print(f'A lista {lista} possui {contador_pares} numeros pares.')
else:
    print(f'a lista {lista} noa possui valores pares.')

