"""
LAMBDAS\\\\\\\\\\\\\\\\\\\\\
Função cujo nao tem nome, função anonima


#COMPARANDO FUÇÃO COM LAMBDA

#FUNÇÃO
def funcao(x):
    return 3 * x + 1


print(funcao(4))

#LAMBDA
lambda x: 3 * x + 1

EXEMPLO 1 DE LAMBDAS\\\\\\\\\\\\\\\\\\\\\\\\\\\\
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('LUIS', '     filipe'))
print(nome_completo('CAio  ', 'augusto'))

EXEMPLO 2 DE LAMBDA\\\\\\\\\\\\\\\\\\\\\\\\

amar = lambda: 'como nao amar python'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 2
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(amar())
print(uma(6))
print(duas(3, 5))
print(tres(4, 6, 7))

EXEMPLO 3 DE LAMBDA\\\\\\\\\\\\\\\\\\\\\\\\\\\\

autores = ['Isaac Asimov', 'Ray Adbala', 'Robert Heilein', 'Arthur C. Clarck', 'Frank Herbert', 'Orson Scott Clarson',
           'Douglas Adams', 'H. G. Hells', 'Leight Braket']

print(autores)

"ORDENAR OS NOMES PELAS INICIAIS DO SOBRENOME"
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

EXEMPLO 4 DE LAMBDA\\\\\\\\\\\\\\\\\\\\\\\\\\\

def funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


teste = funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(3))
print(teste(2))

print(funcao_quadratica(2, 3, -5)(0))

import math


def area(r):
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

EXPRESSAO LAMBDA COM MAP\\\\\\\\\\\\\\\\\\\\\\\\\\

raios = [2, 5, 7.1, 0.3, 10, 44]

"forma comum"
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

"forma 2 - Map"

areas = map(area, raios)

print(list(areas))

"forma 3 com lambda"

print(list(map(lambda r: math.pi * (r ** 2), raios)))


EXEMPLO 5 DE MAP\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

cidades = [('rio de janeiro', 30), ('Manaus', 36), ('londres', 13), ('japao', 22),
          ('rio grande do sul', 25)]

print(cidades)

c_para_f = lambda dado: (dado[0], 9/5 * dado[1] + 32)

print(list(map(c_para_f, cidades)))


EXEMPLO DE FILTER EM LAMBDA\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

import statistics

dados = [3.5, 4.6, 8.6, 8.7, 9.9]

media = statistics.mean(dados)

print(media)

res = filter(lambda x: x > media, dados)
print(list(res))

EXEMPLO 2 DE FILTER \\\\\\\\\\\\\\\\\\\\\\\\\

paises = ['', 'australia', 'belgica', 'brasil', '', 'espanha', 'colombia', 'equador', '']

res = filter(None, paises)

print(list(res))

EXEMPLO 2 DE FILTER \\\\\\\\\\\\\\\\\\\\\\\\\

usuarios = [
    {"username": "samuel", "tweets": ["eu amo pizza", "eu amo meu cachorro"]},
    {"username": "michel", "tweets": []},
    {"username": "lucas", "tweets": ["sou fã do neymar", "vou sair hoje"]},
    {"username": "larissa", "tweets": []},
    {"username": "sjorge", "tweets": ["eu amo hamburguer"]}
]


inativos = list(filter(lambda usuario: len(usuario["tweets"]) == 0, usuarios))

print(inativos)

nomes = ['Vanessa', 'Julia', 'Naja']

lista = list(map(lambda nome: f'sua instrutora é {nome}', filter(lambda nome: len(nome) > 5, nomes)))

print(lista)
"""