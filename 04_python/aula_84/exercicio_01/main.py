from funcoes import *

limpar()

total = int(input("- Digite o total de números que serão analisados: "))


loop = 1

par = 0

impar = 0


while( loop <= total):
  numero = int(input(f"- Digite o {loop}º numero: "))

  loop += 1

  if(numero % 2 == 0):
    par += 1  

  else:
    impar += 1 


print(f"\n---Total de números PARES---: ({par})")
print(f"---Total de números ÍMPARES---: ({impar})")



