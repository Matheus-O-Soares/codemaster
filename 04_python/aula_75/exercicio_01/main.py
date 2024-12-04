import math
import random

print("\n\n")

# Variáveis

original = -10
float_original = 3.567


# Executar

print("=== Funções dos Inteiros === \n")

print("Inteiro 'original' :(" + str(original) + ")")
print("Float 'original' :(" + str (abs(original)) + ")\n")

print("Números inteiro aleatório 'entre 1 e 5' :(" + str(random.randint(1, 5)) + ")")

print("\n")

print("=== Funções dos Floats ===\n")

print("Float 'original' :(" + str (abs(float_original)) + ")\n")

print("Float 'arredondado' :(" + str (round(float_original)) + ")")
print("Float 'original' :(" + str (round(float_original, 1)) + ")")
print("Float 'original' :(" + str (round(float_original, 2)) + ")\n")

print("Arredondado para cima :(" + str (math.ceil(float_original)) + ")")
print("Arredondado para baixo :(" + str (math.floor(float_original)) + ")")


print("\n\n")
