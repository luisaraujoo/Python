"""
EXEMPLO DEFINIÇÃO DE FUNÇÕES\\\\\\\\\\\\\\\\

def diz_oi():
    print('OIII!!')

diz_oi()

EXEMPLO 2 DE DEFINIÇÃO DE FUNÇÕES\\\\\\\\\\\\\\\\\

def cantar_parabens():
    print('PARABÉNS PARA VOCÊ')
    print('NESTA DATA QUERIDA')
    print('MUITAS FELICIDADES')
    print('MUITOS ANOS DE VIDA')
"""

"""
for i in range(2):
    cantar_parabens()

ALGUMAS EXPLICAÇÕES DE FUNÇÕES\\\\\\\\\\\\\\\\\\\\

EXEMPLO1\\
def quadrado_de_10():
    print(10 * 10)


quadrado_de_10()
#nesse exmplo de função ele só vai me retornar o print, e não um valor

EXEMPPLO2\\

def quadrado_de_10():
    return 10 * 10


resultado = quadrado_de_10()
print(resultado)
#nesse exemplo ele ja me retorna um valor da função, pelo uso de RETURN


EXEMPLO3\\

def diz_oi():
    return 'OIII '


alguem = 'Jorge!'

print(diz_oi() + alguem)

EXEMPLO4\\
#Nada na função pode ser executada depois do "return"

def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'OIII '
    print('Estou sendo executado depois do retorno...')


print(diz_oi())

EXEMPLO5\\
def nova_funcao():
    variavel = True
    if variavel is True:
        return 4
    elif variavel is None:
        return 5
    return 6


print(nova_funcao())

EXEMPLO DE FUNÇÃO COM RANDOM\\\\\\\\\\\\\\
from random import random


def jogar_moeda():
    valor = random()
    if valor < 0.5:
        return 'CARA'
    return 'COROA'


print(jogar_moeda())


EXEMPLO DE FUNÇÕES COM PARÂMETROS\\\\\\\\\\\\\\\\\\\

def quadrado(num):
    return num * num

print(quadrado(7))
print(quadrado(80))
print(quadrado(6))


EXEMPLO DE FUNÇÃO COM KEYWORD ARGUMENT\\\\\\\\\\\\\\\\\\\

def nome_completo(nome, sobrenome):
    return f'Seu nome comleto é {nome} {sobrenome}'


nome = 'Luis Felipe'
sobrenome = 'Araujo'

print(nome_completo(nome='Luis', sobrenome='Araujo'))

EXEMPLO DE FUNÇÕES COM PARAMETROS\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 54, 5, 6]
print(soma_impares(lista))


EXEMPLO DE FUNÇÕES COM PARAMETROS PADROES\\\\\\\\\\\\\\\\\\

def exponencial(numero=4, potencia=2):
    return numero ** potencia


print(exponencial(2, 5))
print(exponencial(2)) #por padrão eleve ao quadrado
print(exponencial(5, 10))


EXEMPLO DE FUNCAO COM PARAMETROS PADROES 2 \\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def validacao_de_entrada(nome='Luis Felipe', chefe=True, sobrenome='Araujo'):
    if nome == 'Luis Felipe' and chefe and sobrenome == 'Araujo':
        return 'Bem vindo dono da porra toda! Pode usar o sistema a vontade'
    elif nome == 'Luis Felipe' and chefe is False and sobrenome == 'Araujo':
        return 'Ola Luis Felipe Araujo'
    else:
        return 'Ola, como vai?'


print(validacao_de_entrada(nome='Luis Felipe', chefe=True, sobrenome='Araujo'))
print(validacao_de_entrada(nome='Jose', chefe=True, sobrenome='Araujo'))
print(validacao_de_entrada(nome='Luis Felipe', chefe=False, sobrenome='Araujo'))

EXEMPLO DE FUNÇÕES COM ARGS\\\\\\\\\\\\\\\\\

def somadosnumeros(*args):
    return sum(args)


print(somadosnumeros(40, 85, 873))
print(somadosnumeros(33, 4, 2))

MAIS UM EXEMPLO DE ARGS\\\\\\\\\\\\\\\\\\\\

def verifica_info(*args):
    if 'Luis' in args and 'Felipe' in args:
        return 'Bem vindo Luis'
    else:
        return 'Desculpa, nao sei quem é você'


print(verifica_info('Luis', 1, 'Felipe'))
print(verifica_info(4985, 1, 'Felipe'))
print(verifica_info('carlos', 1, 'Felipe'))


EXEMPLO DE KWARGS\\\\\\\\\\\\\\\\\\\\\\\\\

def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento pythonico'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} geek!"
    return 'Não tenho certeza quem você é...'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='Especial'))


MAIS EXEMPLOS DE KWARG E WARGS\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#É IMPORTANTE A ORDEM DE PARAMETROS NA DECLARAÇÃO
def mostra_info(a, b, *args, instrutor='Luis', **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, nome='lucas', cargo='engenheiro'))


DESEMPACOTAR ARGS É COM * E KWARGS É COM **
desempacotar_dados(*lista, tupla, conjuntos)
desempacotar_dados(**dicionarios)
"""
