import os


#Criação das funções


def fahr(temperatura):
  f = temperatura * 1.8 + 32
  print(f"({f:.1f})\n")

def kelvin(temperatura):
  k = temperatura + 273.15
  print(f"({k:.1f})\n") 


# Funções Especiais 

def limpar():
  if(os.name == "nt"): 
    os.system("cls")
  else: 
    os.system("clear")