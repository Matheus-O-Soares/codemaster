from funcoes import *

limpar()

print("=== Cálculo de Áreas com Funções ===\n")

print("=== Escolha uma opção ===")

print("(t) para triângulos.")
print("(r) para rectângulos.")
print("(c) para círculo.\n")

opçao = input ("Opção:")

animar("A analisar")

if(opçao.lower() == "T"): calcularTri()
elif(opçao.lower() == "r"): calcularRect()
elif(opçao.lower() == "c"):calcularCirc()

else:print("--- Opção Inválida ---")


limpar()


print("\n\n")