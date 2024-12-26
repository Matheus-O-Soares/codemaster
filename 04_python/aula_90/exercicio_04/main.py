from funcoes import *

limpar()

while True:
  opcao = exibirMenu()

  if opcao == "1":
    print("Adicionar Produto")
  elif opcao == "2":
    print("Editar Produto")
  elif opcao == "3":
    print("Apagar Produto")
  elif opcao == "4":
    print("Listar Produtos")
  elif opcao == "0":
    print("Saindo do programa")
    break
  else:
    print("Opção inválida")

  aguardar(2)
  limpar()



print("\n\n")

