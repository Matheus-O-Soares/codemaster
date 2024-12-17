from funcoes import *

limpar()


resposta = ""

loop = 1

while(resposta.lower() !="sim"):
  print("estude para o teste:")
  resposta = input(f"- Você passou no ({loop}º) teste? ")
  if(resposta == "sim"): break
  print()
  loop+= 1

print("Parabéns")
print(f"Você foi aprovado no teste de de nº ({loop})")


print("\n\n")