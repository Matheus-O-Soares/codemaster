import os

import time

import math

#Criação das funções
def calcularTri():
  base = float(input("- Digite a base do triangulo: "))
  altura = float(input("- Digite a altura do triangulo"))
  area = (base * altura) / 2
  animar("A analisar")
  print("===== Cálculo de áreas com funções =====\n")
  print(f"--- A área do triangulo é de ({area:.1f}) ---")


def calcularRect():
  base = float(input("- Digite a base do rectãngulo:"))
  altura = float(input("- Digite a altura do rectãngulo:"))
  area = base * altura
  animar("A analisar")
  print("===== Cálculo de áreas com funções =====\n")
  print(f"--- A área do rectãngulo é de ({area:.1f}) ---")

def calcularCirc():
  raio = float(input("- Digite o raio do círculo: "))
  area = math.pi * raio ** 2
  animar("A analisar")
  print("===== Cálculo de áreas com funções =====\n")
  print(f"--- A área do circulo é de ({area:.1f}) ---")



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

