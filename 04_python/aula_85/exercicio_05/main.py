from funcoes import *

limpar()


inicial = int(input("- Digite o valor inicial de sua lista numérica: "))
final = int(input("- Digite o valor final de sua lista numérica: "))
repeticao = int(input("- Dquantas vezes quer repetir: "))


print()

for i in range(repeticao):

  if inicial < final:
    for j in range(inicial, final +1): print(j)

  else:
    for j in range(inicial, final -1, -1): print(j)

    print("-"*20)



print("\n\n")
