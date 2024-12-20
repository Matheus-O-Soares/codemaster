from funcoes import *

limpar()

lista_1 = ["uva", "maça", "morango", "ananás", "banana", "laranja"]
print()
print("=== lista de Frutas com FOR ===\n")

for f in lista_1: print(f)

print()

print("=== lista de Frutas com FOR + RANGER ===\n")

for i in range(len(lista_1)): 
  print(f"{i+1} - {lista_1[i]}")

print()

print("=== lista de Frutas com FOR + REVERSE() ===\n")

for f in reversed(lista_1): print(f)

print()

print("=== lista de Frutas com FOR + RANGE() Reverso ===\n")

for i in range(len(lista_1)-1, -1, -1):
  print(f"{i+1} - {lista_1[i]}")

print()


