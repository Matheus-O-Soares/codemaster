from funcoes import *

limpar()

alunos = int(input("- Digite o total de alunos da turma: "))

idade = 0
total = 0
loop = 1

while (loop <= alunos):
  idade = int(input(f"- Digite a idade do {loop}º aluno: "))
  loop += 1  
 
  total += idade

media = total / alunos

print()

print(f"A média de idade é ({media:.1f})")
