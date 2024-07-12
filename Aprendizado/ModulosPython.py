"""
MODULO RANDOM

EXEMPLO DE RANDOM COM UNIFORM\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#GERA VALORES REAIS
import random

#random() gera um numero aleatorio entre 0 e 1
print(random.random())


from random import uniform
#do modulo random import a função random

for i in range(10):
    print(uniform(3, 7))

EXEMOPLO DE RANDOM COM RANDINT\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#GERA VALORES INTEIROS
from random import randint

for i in range(10):
    print(randint(1, 62), end=', ')

EXEMPLO DE RANDOM COM CHOICE\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\    

from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))

EXEMPLO COM SHUFFLE\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
from random import shuffle

cartas = ['k', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)

shuffle(cartas)

print(cartas.pop())

EXEMPLO DE APELIDO DE FUNÇÃO\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
from random import randint as rdi, random as rdm
#apelidando a função/módulo
print(rdi(1, 3))

DA PRA IMPORTAR MODULOS EXTRAS DE SITES\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""















