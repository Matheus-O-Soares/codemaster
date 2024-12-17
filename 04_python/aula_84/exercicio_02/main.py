from funcoes import *

limpar()

total = int(input("- Digite o total de números que serão analisados: "))

print()

loop = 1 
maior = 0 
menor = 0

while(loop <= total):
  numero_digitado = int(input(f"-digite numero({loop})"))
  if(loop == 1):
    maior = numero_digitado
    menor = numero_digitado
  else:
    if(numero_digitado > maior): maior = numero_digitado
    elif(numero_digitado < maior): menor = numero_digitado
  loop += 1

print()

print(f"maior ({maior})")
print(f"menor ({menor})")
