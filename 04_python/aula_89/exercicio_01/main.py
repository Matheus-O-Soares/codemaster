from funcoes import *

limpar()

alunos = []

quantidade = int(input("Quantos alunos deseja cadastrar? "))

animar("aguarde...")

for i in range(1, quantidade+1): alunos.append(input(f"- Digite o nome do[a] ({i}º) aluno(a):  "))

quantidade = int(input(f"- Digite o nome do[a] ({i}º) aluno(a):  "))

animar("aguarde...")

alunos.sort()

print("lista ordenada de alunos: ")

for aluno in alunos: print(aluno)
  