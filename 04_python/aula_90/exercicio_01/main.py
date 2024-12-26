from funcoes import *

limpar()

produtos_vetor = ["cadeira","mesa", "caneta"]


produtos_matriz = [
  ["cadeira", 32, 13], ["mesa", 50, 40],["caneta", 0.99, 140],
]

print(produtos_matriz[0] [2])
print(produtos_matriz[2] [0])

print("="*5)

for p in produtos_vetor: print(p)

print("="*5)

for p in produtos_matriz: print(p)

print("="*5)

for p in produtos_matriz:
  print(f"{p[0]} - (preço: {p[1]} - estoque: {p[2]})")

print("="*5)

for linha in produtos_matriz:
  for coluna in linha:
    print(coluna)
    print()


print("\n\n")

