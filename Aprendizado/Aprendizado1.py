"""
IF E ELSE EXEMPLOS
"""
"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
IF SIMPLES 

idade = 18

if idade <= 18:
    print('Ele é maior de idade')

"""
"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
IF COM ELSE

idade = 18

if idade <= 17:
    print('Ele é maior de idade')
else:
    print('Ele é menor de idade')

"""
"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
IF E ELSE COM INPUT(RECEBENDO DADOS)

num1 = int(input("Digite um número: "))
print(num1)

if num1 >= 100:
    print('o numero é maior ou igual a 100')
else:
    print('o numero é menor que 100')

"""
"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
EXEMPLO DE ELIF

nome = 'Jorge'
if nome == 'Luis':
    print('é o Luis')
elif nome == 'Jorge':
    print('é o Jorge')
else:
    print('Não é nenhum dos dois')

"""
"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
EXEMPLO DE FOR

lista = [20, 24, 28, 30]
for num in lista:
    if num == 30:
        print('o numero esta na lista')
    else:
        print('o numero nao esta na lista')

"""
"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
EXEMPLO DE FOR MAIS COMPLEXO

ordens = ['200024', '300051', '523261', '20016546', '3000151', '5689494']

for ordem in ordens:
    if ordem[0] == '2':
        print(f'o numero {ordem} é manutenção')
    elif ordem[0] == '3':
        print(f'o numero {ordem} é prevenção')
    else:
        print(f'o numero {ordem} é correção')

"""
"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
RANGE = (VALOR DE INICIO, VALOR DE PARADA, PASSO)

RANGE EXEMPLO 1

for num in range(11):
    print(num)

RANGE EXEMPLO 2

for num in range(1, 11):
    print(num)

RANGE EXEMPLO 3

for num in range(5, 55, 5):
    print(num)

RANGE EXEMPLO 4
for num in range(10, 0, -1):
    print(num)

"""
"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
EXEMPLO DE WHILE 1
num = 1
while num > 10:
    print(num)
    num = num + 1

EXEMPLO DE WHILE 2

resposta = ''
while resposta != 'sim':
    resposta = input('ja acabou jessica?')

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
EXEMPLO DE BREAK 1
for num in range(1, 11):
    if num == 7:
        break
    else:
        print(num)
print('parei por aqui')

EXEMPLO DE BREAK 2

while True:
    comando = input("digite 'sair' para sair:")
    if comando == 'sair':
        break
print('fim do programa')

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
EXEMPLOS DE LISTAS 1\
lista1 = (range(1, 20))

if 8 in lista1:
    print('encontrei o 8')
else:
    print('nao encontrei o 8')

EXEMPLOS DE LISTAS 2\

lista1 = (range(1, 20))

num = 6
if num in lista1:
    print(f'encontrei o numero {num}')
else:
    print(f'nao encontrei o numero {num}')

EXEMPLOS DE LISTAS 3 COM ORDENAÇÃO DOS NUMEROS DA LISTA\

lista1 = [22, 34, 56, 70, 100, 50]

lista1.sort()
print(lista1)

EXEMPLOS DE LISTAS 4 COM APPEND [ADICIONAR ALGO]\

lista1 = [22, 34, 56, 70, 100, 50]

lista1.append(5)
print(lista1)

EXEMPLO DE LISTA 5 COM EXTEND\

lista1 = [22, 34, 56, 70, 100, 50]
lista1.extend([1, 2, 3])
print(lista1)

EXEMPLO DE LISTAS 6 COM INSERT(ACRESCENTAR UM VALOR EM QUALQUER POSIÇÃO)\

lista1 = [22, 34, 56, 70, 100, 50]
lista1.insert(3, 5)
print(lista1)

EXEMPLO DE LISTAS 7 COM REVERSE\

lista1 = [22, 34, 56, 70, 100, 50]
lista1.reverse()
print(lista1)

EXEMPLO DE LISTA 8 COM LEN(CONTADOR DE ELEMENTOS DA LISTA)\

lista1 = [22, 34, 56, 70, 100, 50]
print(len(lista1))


EXEMPLO DE LISTAS 9 COM POP(TIRA UM ELEMENTO DA LISTA)\

lista1 = [22, 34, 56, 70, 100, 50]
lista1.pop(2)
print(lista1)

EXEMPLO DE LISTAS 10 : MULTIPLICANDO A LISTA\

lista1 = [22, 34, 56, 70, 100, 50]
lista1 = lista1 * 5
print(lista1)

EXEMPLO DE LISTA 11: TRANSFORMANDO A FRASE EM LISTA\
frase = 'eu amo bacon'
frase = frase.split()
print(frase)


EXEMPLO DE LISTA 12: MANEIRA DE SEPARAR UMA STRING NA LISTA\

listanova = ['eu', 'amo', 'bacon']
novalista = '$'.join(listanova)
print(novalista)


\\\\\\\\\\\\\\\\\\\\\\EXEMPLO DE LISTA COM MERCADINHO !IMPORTANTE ESSE EXEMPLO!\\\\\\\\\\\\\\\\\\\\\\\
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto no carrinho ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)
        for produto in carrinho:
            print(f'No seu carrinho tem o produto {produto}')

carrinho2 = ', '.join(carrinho)

print(f"Você acabou suas compras, e no seu carrinho tem: {carrinho2}")


EXEMPLO DE LISTA 13: \\\\\\\\\\

lista1 = [22, 34, 56, 70, 100, 50, 55, 30, 48]
print(lista1[1::2]) ### COMEÇANDO DE 1 E INDO ATÉ O FINAL DE 2 EM 2

lista1 = [22, 34, 56, 70, 100, 50, 55, 30, 48]
print(lista1[::2]) ### COMEÇANDO EM E INDO ATÉ O FINAL DE 2 EM 2


DESEMPACOTAMENTO DE TUPLAS\\\\\\\\\\\\\\

tupla = (30, 40, 50)
num1, num2, num3 = tupla
print(num1)
print(num2)
print(num3)

VALORES DENTRO DE UMA TUPLA\\\\\\\\\\\\\

tupla1 = (10, 30, 59, 49, 90)

print(sum(tupla1))
print(max(tupla1))
print(min(tupla1))
print(len(tupla1))


EXEMPLO DE TUPLAS 2 \\\\\\\\\\\\\\\
tupla1 = (10, 30, 59, 49, 90)

for n in tupla1:
    print(n)

for indice, valor in enumerate(tupla1):
    print(indice, valor)

EXEMPLO DE TUPLAS 3\\\\\\\\\\\\\\\\\\
frase = tuple('EU TE AMO PARA SEMPRE')
print(frase.count('E'))

EXEMPLO DE TUPLA COM WHILE\\\\\\\\\\\\\\

meses = ('Janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

print(meses[6])
print(type(meses))
print(len(meses))

i = 0
while i < len(meses): #len é o numero de elementos em uma lista ou tupla
    print(meses[i])
    i = i + 1

EXEMPLO DE TUPLA COM INDEX\\\\\\\\\\\\\\\\\

meses = ('Janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

print(meses.index('março'))

EXEMPLO DICIONARIO 1\\\\\\\\\\\\\\\\\\\\\

paises = {'br': 'Brasil', 'eua': 'Estados Unidos'}
print(paises)


DESEMPACOTANDO DICIONARIOS\\\\\\\\\\\\\\\\\\\\\\\\\\\
paises = {'br': 'Brasil, Canada', 'eua': 'Estados Unidos'}
print(paises['br'])
print(paises['eua'])


EXEMPLO DICIONARIO 2\\\\\\\\\\\\\\\\\\\\\\

paises = {'br': 'Brasil, Canada', 'eua': 'Estados Unidos'}

pais = paises.get('br')

if pais:
    print(f'encontrei os paises {pais}')
else:
    print('não encontrei os paises')

Acrescentando um dado em dicionário\\\\\\\\\\\\\\\\\\\\

#forma 1 
receita = {'abr': 200, 'mai': 350, 'jun': 420}

receita['jul'] = 600

print(receita)
#forma 2
novomes = {'ago': 500}
receita.update(novomes)

print(receita)


REMOVER DADO DE DICIONARIO\\\\\\\\\\\\\\\\\\\\
receita = {'abr': 200, 'mai': 350, 'jun': 420}

receita.pop('abr')

print(receita)


"O DICIONARIO CONSEGUE COLOCAR MAIS INFORMAÇÕES DENTRO"\\\\\\\\\\\\\\\\



INTERAR SOBRE DICIONÁRIOS\\\\\\\\\\\\\\\\\\\\\\\\

receita = {'abr': 200, 'mai': 350, 'jun': 420}

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'No periodo de {chave} eu recebi {receita[chave]}')


EXEMPLO E DE MAPAS\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
receita = {'abr': 200, 'mai': 350, 'jun': 420}

for valor in receita.values():
    print(valor)

EXEMPLO 3 DE MAPA\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

receita = {'abr': 200, 'mai': 350, 'jun': 420}

for chave, valor in receita.items():
    print(f'chave = {chave} e valor = {valor}')

EXEMPLO 4 DE MAPA

receita = {'abr': 200, 'mai': 350, 'jun': 420}

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))

EXEMPLO DE SET(CONJUNTO)\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

s = ({1, 2, 3, 3, 4, 5, 6, 7, 8})

print(s)
print(type(s))

EXEMPLOS E COMPARAÇÕES DE LISTA, TUPLA, DICT, E SET\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

lista = [1, 2, 3, 3, 44, 5, 6, 7, 10]
print(f'lista {lista} com {len(lista)} elementos')

tupla = 1, 2, 3, 3, 44, 5, 6, 7, 10
print(f'tupla {tupla} com {len(tupla)} elementos')

dicionario = {}.fromkeys([1, 2, 3, 3, 44, 5, 6, 7, 10], 'valor')
print(f'dicionario {dicionario} com {len(dicionario)} elementos')

conjunto = {1, 2, 3, 3, 44, 5, 6, 7, 10}
print(f'lista {conjunto} com {len(conjunto)} elementos')

EXEMPLOS DE UTILIZAÇÃO DO SET EM UMA LISTA\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

cidades = ['Rio de Janeiro', 'Belo Horizonte', 'São Paulo', 'Pernanbuco', 'Rio de Janeiro', 'São Paulo']
print(len(cidades))

# Agora eu quero saber quantas cidades de fato foram cadastradas

print(len(set(cidades)))

ADICIONAR NUMEROS NO SET (.add())\\\\\\\\\\\\\\\\\\\\\\

s = {1, 2, 3}

s.add(4)

print(s)

REMOVER NUMEROS NO SET (.remove())\\\\\\\\\\\\\\\\\\\\\\

s = {1, 2, 3}

s.remove(3)

print(s)

EXEMPLOS 4 DE SET\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

estudantes1 = {'luis', 'Amanda', 'jorge', 'Leticia'}
estudantes2 = {'Carol', 'Amanda', 'Lucas', 'Miguel'}

unicos = estudantes1.union(estudantes2)
print(unicos)

ambos = estudantes1.intersection(estudantes2)
print(ambos)

so_os_que_estudam_somente_no_1 = estudantes1.difference(estudantes2)
print(so_os_que_estudam_somente_no_1)

COUNTER COLLECTIONS EXEMPLO 1\\\\\\\\\\\\\\\\\\\\\\\\\\\

from collections import Counter

lista = [1, 1, 1, 1, 3, 4, 5, 67, 76, 4, 23, 4, 4565, 77, 8, 7, 9, 89, 4, 2, 3, 3, 34]

resultado = Counter(lista)

print(resultado)

EXEMPLO MUDULO COLLECTIONS\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

from collections import Counter

texto = Pelé começou a jogar pelo Santos Futebol Clube aos quinze anos de idade, e pela Seleção Brasileira aos
#dezesseis. Durante sua carreira na Amarelinha,sagrou-se campeão de três edições da Copa do Mundo FIFA: 1958, 1962 e
#1970, sendo o único a fazê-lo como jogador.

#SEPARO TODAS AS PALAVRAS QUE TENHO NO TEXTO, UMA A UMA
palavras = texto.split()

palavras2 = Counter(palavras)

#A QUANTIDADE QUE CADA PALAVRA APARECE NO TEXTO
print(palavras2)

#AS 5 PALAVRAS QUE MAIS SE REPETEM
print(palavras2.most_common(5))

EXEMPLO DEFAULTDICT\\\\\\\\\\\\\\\\\\\\\\\\\\

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em python'

print(dicionario)

print(dicionario['outro'])

EXEMPLO NAMEDTUPLE\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

from collections import namedtuple

cachorro = namedtuple('cachorro', ['nome', 'idade', 'raça'])

jorgin = cachorro(nome='jorgin', idade='10', raça='pitbul')

print(jorgin.nome)
print(jorgin.idade)
print(jorgin.raça)

EXEMPLO DE DEQUE\\\\\\\\\\\\\\\\\\\\\

from collections import deque

nome = deque('geek')
nome.append('y')
print(nome)
nome.appendleft('G')
print(nome)


EXEMPLO DEFINIÇÃO DE FUNÇÕES\\\\\\\\\\\\\\\\]

def diz_oi():
    print('OIII!!')

diz_oi()

EXEMPLO 2 DE DEFINIÇÃO DE FUNÇÕES\\\\\\\\\\\\\\\\\

def cantar_parabens():
    print('PARABÉNS PARA VOCÊ')
    print('NESTA DATA QUERIDA')
    print('MUITAS FELICIDADES')
    print('MUITOS ANOS DE VIDA')


for i in range(2):
    cantar_parabens()

ALGUMAS EXPLICAÇÕES DE FUNÇÕES\\\\\\\\\\\\\\\\\\\\

EXEMPLO1\\
def quadrado_de_10():
    print(10 * 10)


quadrado_de_10()
#nesse exmplo de função ele só vai me retornar o print, e não um valor 

EXEMPPLO2\\\

def quadrado_de_10():
    return 10 * 10


resultado = quadrado_de_10()
print(resultado)
#nesse exemplo ele ja me retorna um valor da função, pelo uso de RETURN

"""
