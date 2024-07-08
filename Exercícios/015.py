listanotas = []

while len(listanotas) < 15:
    nota = float(input(f'adicione a nota do aluno {len(listanotas) + 1}/15: '))
    listanotas.append(nota)

print(f'a média de notas dos alunos é {"%.2f" % (sum(listanotas)/15)}')