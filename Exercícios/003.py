"""Faça um programa que tenha uma função que recebe uma data no formato string exemplo “01/01/2024” e
imprima ela por extenso como “1 de janeiro de 20204”."""

def por_extenso(data: str) -> None:
    d = data.split('/')

    dia: int = int(d[0])
    mes: int = int(d[1])
    ano: int = int(d[2])

    if mes == 1:
        mes_strg = 'janeiro'
    elif mes == 2:
        mes_strg = 'fevereiro'
    elif mes == 3:
        mes_strg = 'março'
    elif mes == 4:
        mes_strg = 'abril'
    elif mes == 5:
        mes_strg = 'maio'
    elif mes == 6:
        mes_strg = 'junho'
    elif mes == 7:
        mes_strg = 'julho'
    elif mes == 8:
        mes_strg = 'agosto'
    elif mes == 9:
        mes_strg = 'setembro'
    elif mes == 10:
        mes_strg = 'outubro'
    elif mes == 11:
        mes_strg = 'novembro'
    elif mes == 12:
        mes_strg = 'dezembro'
    else:
        mes_strg = 'desconhecido'


    print(f'{dia} de {mes_strg} de {ano}')


por_extenso('05/12/2052')

