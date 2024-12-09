import os

#Criação das funções


def calcularfahr(f, c ):
  fahren = f = c * 1.8 + 32
  print(f"O IMC é ({fahren:.1f})\n")

def calcularkelvin(k, c):
  kelvin = k = c + 273.15
  print(f"--- ({kelvin:.1f})\n")  




# Funções Especiais 

def limpar():
  if(os.name == "nt"): 
    os.system("cls")
  else: 
    os.system("clear")