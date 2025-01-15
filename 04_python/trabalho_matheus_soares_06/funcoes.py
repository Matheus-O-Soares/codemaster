import os
import time
import globais


# Criação das Funções
def exibirMenu():
  animar("Aguarde")
  print(f"=== {globais.empresa} ===\n")
  print("1 - Registar produto.")
  print("2 - Editar produto.")
  print("3 - Apagar produto.")
  print("4 - Listar produtos.\n")
  print("5 - Vender.")
  print("6 - Listar vendas.\n")
  print("0 - Sair.\n")

produtos = {}

def registarProduto():
  global produtos  
  print("--- Registar Produto ---\n")
  nome = input("- Digite o nome do novo produto: ")
  preco = float(input("- Digite o preço deste produto: "))
  quantidade = int(input("- Digite a quantidade deste produto: "))
  produtos[nome] = {'preco': preco, 'quantidade': quantidade}
  print("\n--- SUCESSO! ---")
  aguadar(2)

def editarProduto():
  global produtos  # Declara que estamos usando a variável global
  print("--- Editar Produto ---\n\n")
  listaProdutos()

  
  if not produtos:
    return  # Se não houver produtos, não faz nada

  nome_produto = input("\n- Digite o nome do produto que queres editar: ")
  
  if nome_produto in produtos:
    while True:
      print(f"\n--- Menu de Edição --- \n")
      print("1 - Nome.")
      print("2 - Preço.")
      print("3 - Quantidade.")
      print("\n0 - Voltar.")
      opcao_edicao = input("\n- opção: ")

      if opcao_edicao == "1":
        novo_nome = input("\nDigite o novo nome do produto: ")
        produtos[novo_nome] = produtos.pop(nome_produto)  # Atualiza o nome
        nome_produto = novo_nome  # Atualiza a variável para o novo nome
        print(f"\nNome do produto editado para {novo_nome}.")

      elif opcao_edicao == "2":
        while True:
          novo_preco = input("\nDigite o novo preço do produto: ")
          if novo_preco.replace('.', '', 1).isdigit():  # Verifica se é um número
            produtos[nome_produto]['preco'] = float(novo_preco)  # Atualiza o valor
            print(f"\nPreço do produto editado para: {produtos[nome_produto]['preco']:.2f} €.")
            break
          else:
            print("\nPreço inválido. Tente novamente.")

      elif opcao_edicao == "3":
        while True:
          nova_quantidade = input("\nDigite a nova quantidade do produto: ")
          if nova_quantidade.isdigit():  # Verifica se é um número
            produtos[nome_produto]['quantidade'] = int(nova_quantidade)  # Atualiza a quantidade
            print(f"\nQuantidade do produto atualizada para {produtos[nome_produto]['quantidade']}.")
            break
          else:
            print("\nQuantidade inválida. Tente novamente.")

      elif opcao_edicao == "0":
        print("\nVoltando ao menu principal...")
        break

      else:
        print("\nOpção inválida. Tente novamente.")
  else:
    print(f"Produto '{nome_produto}' não encontrado.")

def apagarProduto():
  global produtos  # Declara que estamos usando a variável global
  listaProdutos()
  
  if not produtos:
    return  # Se não houver produtos, não faz nada

  nome_produto = input("\n- Digite o nome do produto que deseja apagar: ")
  
  if nome_produto in produtos:
    produtos.pop(nome_produto)  # Remove o produto
    print("\n--- SUCESSO! ---")
  else:
    print(f"\nProduto {nome_produto} não encontrado.")

def listaProdutos():
  if not produtos:
    print("--- lista de Produto ---")
    print("\nNenhum produto na lista.")
  else:
    print("--- listar Produto ---\n")
    for i, (nome, info) in enumerate(produtos.items()):
      print(f"#{i+1} - (Nome: {nome}) (Preço: {info['preco']:.2f} €) (Quantidade: {info['quantidade']}).")

def verificarSaldo():
  print("--- Saldo ---\n")
  print(f"Saldo atual: ( {globais.saldo:.2f} € )\n")
  print(globais.historico)
  primaEnter()


















# Funções Especiais
def limpar():
  if(os.name == "nt"): os.system("cls")
  else: os.system("clear")

def aguadar(segundos): time.sleep(segundos)

def primaEnter(): input("\nCarregue <ENTER> para continuar...")

def animar(frase):
  tempo = 0.3
  limpar()
  print(f"\n{frase}", end="", flush=True)
  aguadar(tempo)
  print(".", end="", flush=True)
  aguadar(tempo)
  print(".", end="", flush=True)
  aguadar(tempo)
  print(".", end="", flush=True)
  aguadar(tempo)
  limpar()