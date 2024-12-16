from funcoes import *

limpar()

resposta = input("- Desejas tirar a carta de condução ?")

if(resposta == "sim"):
  teste = 1
  aprovado = False

  while not aprovado:
    print(f"Estudar para o ({teste}º) teste")
    resultado = input(f"-Você passou no ({teste}º) teste?")

    if(resultado == "sim"):
      aprovado = True
      print(f"Parabéns! foi aprovado no ({teste}º) teste.")

    else:
      teste += 1

else:
  print("Utilize transportes públicos")


print("\n\n")