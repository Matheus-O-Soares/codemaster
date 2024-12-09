import os


#Criação das funções




# Funções Especiais 

def limpar():
  if(os.name == "nt"): 
    os.system("cls")
  else: 
    os.system("clear")

def aguardar(segundos): time.sleep(segundos)