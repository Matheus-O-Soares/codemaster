print("\n\n")


# Variáveis
nome = input("- Digite o nome do paciente: ")
peso = float(input("- Digite o peso do paciente (kg): "))
altura = float(input("- Digite o altura do paciente (m): "))

imc = peso / altura ** 2


# Executar 

print("\n")

print(f"O paciente ({nome}) está com um IMC de ({imc:.1f}).")






print("\n\n")