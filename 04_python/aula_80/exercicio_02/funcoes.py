import os

import time

#Criação das funções
def verificarResposta_1(idade, conhecimento):
  if(idade >= 18 and conhecimento.lower() == "sim"):
    return "aprovado para candidatura"
  
  elif (idade < 18 and conhecimento.lower() == "nao"):
  return "aprovado para escola de programadores"

# Funções Especiais 

def limpar():
  if(os.name == "nt"): 
    os.system("cls")
  else: 
    os.system("clear")

def aguardar(segundos): time.sleep(segundos)