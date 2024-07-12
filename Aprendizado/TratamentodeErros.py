"""
UTILZANDO RISE PARA ESPECIFICAR O ERRO\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('a cor precisa ser uma string')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('joven', 'azul')
colore('jabulani', 'amarelo')
colore('amor', 3)

EXEMPLO 2 COM VALUE\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'roxo')
    if type(texto) is not str:
        raise TypeError('texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('a cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'a cor precisa ser uma entre: {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')


colore('luis', 'preto')

try/except\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


try:
    len(5)
except:
    print('Deu algum problema')

    
JEITO CERTO DE FAZER, POIS VOCE ESPECIFICA O ERROR\\\\\\\\\\\\\\\\\\\\\\

try:
    geek()
except NameError:
    print('Voce esta utilizando uma função inexistente')

ESPECIFICANDO VARIOS ERROS\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

try:
    geek()
except NameError as err1:
    print(f'Deu NameError: {err1}')
except TypeError as err2:
    print(f'Deu TypeError: {err2}')
except:
    print('Deu algum erro diferente')

EXEMPLO 3\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\    

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {'nome': 'Geek'}

print(pega_valor(dic,'nome'))
print(pega_valor(dic, 6))

EXEMPLO 4\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
try:
    num = int(input('informe um numero: '))
    print(f'seu numero digitado foi {num}')
except ValueError:
    print('Valor incorreto')

EXEMPLO 5 MAIS COMPLEXO\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def dividir(a, b):
    return a / b


num1 = int(input('Informe o primeiro numero: '))

try:
    num2 = int(input('Informe o segundo numero: '))
except ValueError:
    print('O valor precisa ser numerico')

try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

EXEMPLO 6 MAIS COMPLEXO\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\    
    
def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'

num1 = input('Digite o valor do primeiro numero: ')
num2 = input('Digite o valor do segundo numero: ')

print(dividir(num1, num2))

EXMPLO RESUMIDO\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError):
        return 'Ocorreu um problema'

num1 = input('Digite o valor do primeiro numero: ')
num2 = input('Digite o valor do segundo numero: ')

print(dividir(num1, num2))

DEBUGGANDO COM PDB\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação'
final = nome_completo + 'faz o curso' + curso
print(final)
"""


