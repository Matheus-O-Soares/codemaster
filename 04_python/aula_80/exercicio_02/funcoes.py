import os

import time

#Criação das funções
def verificarStatus(idade, conhecimento):
  if(idade >= 18 and conhecimento.lower() == "sim"):
    return "aprovado para candidatura"
  
  elif (idade < 18 and conhecimento.lower() == "nao"):
    return "aprovado para escola de programadores"

   elif (idade < 18 and conhecimento.lower() == ""):
    return "aprovado para escola de programadores"

# Funções Especiais 

def limpar():
  if(os.name == "nt"): 
    os.system("cls")
  else: 
    os.system("clear")

def animar(frase): 
  tempo = 0.3
  print(frase:)