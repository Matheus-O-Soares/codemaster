from funcoes import *

opcao = None
while(opcao != "0"):

  exibirMenu()
  opcao = input("- Opção: ")

  animar("Aguarde")

  if(opcao == "1"): registarProduto()
  elif(opcao == "2"): editarProduto()
  elif(opcao == "3"): verificarSaldo()
  elif(opcao == "4"): listarProdutos()
  elif(opcao == "5"): ()
  elif(opcao == "6"): verificarSaldo()
  elif(opcao == "0"): 
    animar("A sair")
    break
  else:
    print("--- OPÇÃO INVÁLIDA! ---")
    aguadar(3)

  primaEnter()




print("\n\n")
