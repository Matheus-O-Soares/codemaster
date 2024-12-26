import os

import time

#Criação das funções

def exibirMenu():
  animar("aguarde")
  print("=== Menu ===")
  print("1 - Adicionar Produto")
  print("2 - editar Produtos")
  print("3 - apagar Produto")
  print("4 - listar produtos")
  print("0 - sair\n")
  return (input("opção: "))



# pseudo_construtor
def novoProduto(nome, preco, quantidade):
  novo_produto = [nome, preco, quantidade]
  return novoProduto



# Funções Especiais 

def limpar():
  if(os.name == "nt"): 
    os.system("cls")
  else: 
    os.system("clear")

def aguardar(segundos): time.sleep(segundos)

def animar(frase):
  tempo = 0.3 
  print(frase, end="", flush=True)
  aguardar(tempo)
  print(".", end="", flush=True)
  aguardar(tempo)
  print(".", end="", flush=True)
  aguardar(tempo)
  print(".", end="", flush=True)
  aguardar(tempo)
  limpar()