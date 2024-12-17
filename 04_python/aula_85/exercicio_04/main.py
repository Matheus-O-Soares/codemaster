from funcoes import *

limpar()


inicial = int(input("- Digite o valor inicial de sua lista numérica: "))
final = int(input("- Digite o valor final de sua lista numérica: "))

print()

if inicial < final:
  for i in range(inicial, final +1): print(i)

else:
  for i in range(inicial, final -1, -1): print(i)








print("\n\n")
