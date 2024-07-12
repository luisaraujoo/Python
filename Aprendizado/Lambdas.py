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

EXEMPLO 4 DE LAMBDA\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

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

EXPRESSAO LAMBDA COM MAP\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

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


EXEMPLO 5 DE MAP\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

cidades = [('rio de janeiro', 30), ('Manaus', 36), ('londres', 13), ('japao', 22),
          ('rio grande do sul', 25)]

print(cidades)

c_para_f = lambda dado: (dado[0], 9/5 * dado[1] + 32)

print(list(map(c_para_f, cidades)))


EXEMPLO DE FILTER EM LAMBDA\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

import statistics

dados = [3.5, 4.6, 8.6, 8.7, 9.9]

media = statistics.mean(dados)

print(media)

res = filter(lambda x: x > media, dados)
print(list(res))

EXEMPLO 2 DE FILTER \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

paises = ['', 'australia', 'belgica', 'brasil', '', 'espanha', 'colombia', 'equador', '']

res = filter(None, paises)

print(list(res))

EXEMPLO 2 DE FILTER \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

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

EXEMPLO DE REDUCE\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

from functools import reduce

dados = [1, 2, 4, 5, 6, 7, 8, 9, 10]

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

ANY E ALL \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

EXEMPLO DE ALL = SE TODOS OS ELEMENTOS DO ITERAVEL SAO TRUE\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

print(all([1, 3, 4, 5, 6, 7, 7]))
print(all([0, 3, 4, 5, 6, 7, 7]))
print(all({}))
print(all('Geek'))

EXEMPLO 2 DE ALL\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

nomes = ['carlos', 'cristina', 'cassiano', 'carla']

print(all([nome[0] == 'c' for nome in nomes]))


O any só vai retornar False se tiver um False na lista

GENERATORS\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
É MUITO PARECIDO COM LIST COMPREHENSION, MAS OCUPA MENOS ESPAÇO NA MEMÓRIA

nomes = ['carlos', 'cristina', 'cassiano', 'carla', 'vanessa']

#List comprehension
res = [nome[0] == 'c' for nome in nomes]
print(type(res))

#Generator
res = (nome[0] == 'c' for nome in nomes)
print(type(res))

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
from sys import getsizeof

# Mostra quantos bytes a string geek estas ocupando
print(getsizeof('Geek'))
print(getsizeof('23'))
print(getsizeof('Geek University'))

# COMPARAÇÃO ENTRE COMPREHENSIONS\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
from sys import getsizeof

#list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])
set_comp = getsizeof({x * 10 for x in range(1000)})
dict_comp = getsizeof({x: x * 10 for x in range(1000)})
list_generator = getsizeof(x * 10 for x in range(1000))

print('Para realizar a mesma tarefa, gasttamos de memoria: ')
print(f'List comprehension {list_comp}')
print(f'Set {set_comp}')
print(f'Dicionarios {dict_comp}')
print(f'Generator {list_generator}')

# ORDENAÇÃO DE LISTA, TUPLA, DICT E ETC COM "sorted"\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

usuarios = [
    {"username": "samuel", "tweets": ["eu amo pizza", "eu amo meu cachorro"]},
    {"username": "michel", "tweets": [], "cor": "amarelo"},
    {"username": "lucas", "tweets": ["sou fã do neymar", "vou sair hoje"]},
    {"username": "larissa", "tweets": []},
    {"username": "sjorge", "tweets": ["eu amo hamburguer"], "cor": "azul"}
]

print(sorted(usuarios, key=lambda usuario: usuario["username"]))
print(usuarios)


#ALTERANDO O QUE O MAX E MIN VAO FAZER\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

nomes = ['Luis', 'Carlos', 'Tim', 'Americano', 'Julio']

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))

ABS E ROUND\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#O abs sempre retornar o valor inteiro positivo

print(abs(-5))
print(abs(-3.14))
print(abs(-7))

#O numero com round fica arredondado
print(round(5.12334345))
print(round(3.14))
print(round(7.696756))
"""









