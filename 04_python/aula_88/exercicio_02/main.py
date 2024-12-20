produtos = ["mesa", "cadeira", "papel", "caneta"]
extra = ["bifana", "frango", "bovino"]
print(produtos)

print(produtos)

produtos.sort()
print(produtos)


produtos.sort(reverse=True)
print(produtos)


if("cadeira" in produtos): print("Existe cadeira")
else: print("Não existe cadeira")

#produtos += extra
produtos.extend(extra)
print(produtos)

produtos.clear()
print(print)

