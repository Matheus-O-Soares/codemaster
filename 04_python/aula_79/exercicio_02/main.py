from funcoes import *

limpar()

temperatura = float(input("- Digite uma temperatura em Celsius: "))

print("\n")

converter = (input("- Você deseja converter para (K)elvin ou (F)ahrenheit?"))

if (converter.lower() == "f"):
  fahr(temperatura)

elif (converter.lower() == "k"):
  kelvin(temperatura)
