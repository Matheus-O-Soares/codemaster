from funcoes import *

limpar()


frutas = ["uva", "maça", "morango", "uva", "maça", "morango"]
for f in frutas: print(f)

print("="*20)

for i in range(len(frutas)): 
  print(f"{i+1} - {frutas[i]}")

print("="*20)

for f in reversed(frutas): print(f)

print("="*20)

for i in range(len(frutas)-1, -1, -1):
  print(f"{i+1} - {frutas[i]}")

print("\n\n")