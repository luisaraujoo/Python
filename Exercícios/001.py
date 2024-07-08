"""1. Crie um programa que tenha uma função que recebe um parâmetro inteiro e devolve o seu dobro."""


def dobro_do_parametro(numero=int):
    return f'o dobro do numero {numero} é {numero * 2}'


print(dobro_do_parametro(numero=200))
