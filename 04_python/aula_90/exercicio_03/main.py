from funcoes import *

limpar()

matriz_original = [["Fabrício", 28 , "covilhã"], ["João", 30, "Guarda"], ["Maria", 25, "Covilhã"]]

print("=== listagem das pessoas na matriz ===\n")

for p in matriz_original:
  print(f"{p[0]} - (idade: {p[1]} - Morada: {p[2]})")

print("\n\n")

