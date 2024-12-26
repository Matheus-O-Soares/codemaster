from funcoes import *

limpar()

matriz_original = [
  ["morango", "banana", "uva"], 
  ["frango", "bifana", "novilho"], 
  ["água", "cola", "pepsi"]
]


print("=== for para cada lista dentro da matriz ===\n")

for p in matriz_original:
  print(p)

print()

print("=== for para cada item dentro de cada lista ===\n")
for p in matriz_original:
  for q in p: print(q)
  print()

