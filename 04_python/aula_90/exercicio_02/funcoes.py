import os

import time

#Criação das funções






    



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