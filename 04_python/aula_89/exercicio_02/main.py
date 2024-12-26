from funcoes import *

limpar()

numeros_de_pessoas = int(input('Quantos nomes deseja gerar? '))

import random

# Lista de nomes predefinidos
nomes = ["Ana", "Carlos", "João", "Maria", "José", "Luiza", "Pedro", "Gabriela", "Lucas", "Beatriz"]

# Gerar lista com 10 nomes aleatórios
numeros_de_pessoass = random.sample(nomes, 10)  # Ou random.choices(nomes, k=10) para permitir repetições

print(numeros_de_pessoass)