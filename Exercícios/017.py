valores = []

while len(valores) < 5:
    valor = int(input(f'digite 5 valores {len(valores) + 1}/5: '))
    valores.append(valor)

print(f'A lista contem os valores {valores}, o maior valor é {max(valores)}, o menor valor é {min(valores)} ja a media '
      f'dos numeros é {sum(valores) / 5}')