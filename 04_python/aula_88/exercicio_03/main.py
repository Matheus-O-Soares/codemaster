from funcoes import *

limpar()

lista_1 = ["uva", "maça", "morango", "ananás", "banana", "laranja"]
lista_2 = ["bolo", "pão", "queijo"]

lista_1.sort()
print(f"lista 1: {lista_1}\n")

lista_1.sort(reverse=True)
print(f"lista 1 reversa: {lista_1}\n")

if("morango" in lista_1): 
  print("morango está na lista 1")

print()

lista_1.extend(lista_2)
print(f"lista 1 extendida: {lista_1}\n")


lista_1.clear()
print(f"lista 1 limpa: {lista_1}\n")

