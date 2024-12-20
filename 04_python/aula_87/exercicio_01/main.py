from funcoes import *

opcao = None
while(opcao != "0"):

  exibirMenu()
  opcao = input("- Opção: ")

  animar("Aguarde")

  if(opcao == "1"): registarVenda()
  elif(opcao == "2"): verificarSaldo()
  elif(opcao == "0"): 
    animar("A sair")
    break
  else:
    print("--- OPÇÃO INVÁLIDA! ---")
    aguadar(3)

  primaEnter()





print("\n\n")