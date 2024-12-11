import os

import time

#Criação das funções
def descontar10(valor):
  novo_valor = valor * 0.9
  print(f"{novo_valor:.2f}")

def descontar10Especial(valor):
  novo_valor = valor * 0.9
  return novo_valor


# Funções Especiais 

def limpar():
  if(os.name == "nt"): 
    os.system("cls")
  else: 
    os.system("clear")

def aguardar(segundos): time.sleep(segundos)