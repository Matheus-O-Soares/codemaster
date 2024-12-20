

produto_1 = "mesa"
produto_2 = "cadeira"
produto_3 = "papel"
produto_4 = "caneta"

produtos = ["mesa", "cadeira", "papel", "caneta"]
print(produtos)


produtos[2] = "lapis"
print(produtos)


#adicionar 
produtos.append("x-acto")
print(produtos)

#adicionar lugar especifica
produtos.insert(0, "papel")
print(produtos)

#remover
produtos.pop()
print(produtos)

#remover especifico
produtos.pop(1)
print(produtos)

#remover sem saber posicao
produtos.remove("cadeira")
print(produtos)


