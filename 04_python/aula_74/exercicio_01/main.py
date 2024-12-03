print("\n\n")

# Variáveis

frase = "Boa noite Codemaster!"

# Executar 

print("=== Métodos e Funções das Strings ===\n")

print("String 'original' : ("  + frase + ")\n")

print("String 'capitalizada' : ("  + frase.capitalize() + ")")
print("String 'minúsculas' : ("  + frase.lower() + ")")
print("String 'title' : ("  + frase.title() + ")")
print("String 'maiúsculas' : ("  + frase.upper() + ")\n")

print("String 'total de letras e' : ("  + str(frase.count("e")) + ")")
print("String 'tamanho total com função' : ("  + str(len(frase)) + ")\n")

print("String 'substitui (e) por (X)' : (" + frase.replace ("e", "X") + ")")


print(frase.replace ("o", "%"))

print("\n\n")
