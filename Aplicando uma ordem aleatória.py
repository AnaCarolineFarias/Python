import random

alunos = [
    input("Digite o nome do primeiro aluno: "),
    input("Digite o nome do segundo aluno: "),
    input("Digite o nome do terceiro aluno: "),
    input("Digite o nome do quarto aluno: ")
]
random.shuffle(alunos)

print("A ordem de apresentação será:", alunos)
