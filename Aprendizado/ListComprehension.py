"""
Sintaxer da List Comprehension

[dado for dado in iterável]

EXEMPLO 1 DE LIST COMPREHENSION\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

numeros = [1, 3, 4, 5, 6, 7, 8, 9, 10]

res = [num * 10 for num in numeros]

print(res)

EXEMPLO 2 DE LIST COMPREHENSION\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def funcao(valor):
    return valor * valor


numeros = [1, 3, 4, 5, 6, 7, 8, 9, 10]

res = [funcao(num) for num in numeros]

print(res)

EXEMPLO 3 DE LIST COMPREHENSION\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


nome = 'luis felipe'

print([letra.upper() for letra in nome])

EXEMPLO 3 DE LIST COMPREHENSION\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
colocando em letra maiuscula a inicial das strings

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['jose', 'maria', 'joao']

print([caixa_alta(nome) for nome in amigos])

EXEMPLO 4 DE LIST COMPREHENSION\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

numeros = [1, 3, 4, 5, 6, 7, 8, 9, 10]

pares = [num for num in numeros if num % 2 == 0]
impares = [num for num in numeros if num % 2 != 0]

print(pares)
print([num for num in numeros if num % 2 != 0])

res = [num * 2 if num % 2 == 0 else num / 2 for num in numeros]
print(res)

EXEMPLO DE LISTA ANINHADAS COM LC\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[[print(valor) for valor in lista] for lista in listas]


EXEMPLOS 5 DE LIST COMPREHENSION\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#gerando um tabulerio
tabuleiro = [[numero for numero in range(1, 5)] for valor in range(1, 5)]
print(tabuleiro)

#gerando jogadas para o jogo da velha
velha = [['X' if numero % 2 == 0 else '0' for numero in range(1, 4)]for valor in range(1, 4)]
print(velha)

#gerando valor iniciais
print([['*' for i in range(1, 4)]for j in range(1, 4)])

EXEMPLOS 6 DE dict COMPREHENSION\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

numeros = {'num1': 4, 'num2': 3, 'num5': 6}

quadrados = {j: i ** 2 for j, i in numeros.items()}

print(quadrados)


EXEMPLOS 7 DE dict COMPREHENSION\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


numeros = [1, 3, 4, 5, 6, 7, 8, 9, 10]

resultado = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}

print(resultado)
"""