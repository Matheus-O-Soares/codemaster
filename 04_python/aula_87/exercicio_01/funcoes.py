import os
import time
import globais


# Criação das Funções
def exibirMenu():
  animar("Aguarde")
  print(f"=== {globais.empresa} ===\n")
  print("1 - Vender.")
  print("2 - Ver histórico.\n")
  print("0 - Sair.\n")

def registarVenda():
  print("--- Vender ---\n")
  descricao = input("- Descrição da venda: ")
  valor = float(input("- Digite o valor total da venda: "))
  if(valor > 0):
    globais.saldo += valor
    globais.historico += f"#Venda - {descricao} ( {valor:.2f} € )\n"
    print("\n--- SUCESSO! ---")
    aguadar(2)

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

def primaEnter(): input("\nPRIMA ENTER PARA CONTINUAR...")

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