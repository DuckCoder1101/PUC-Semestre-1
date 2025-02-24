comp = float(input("Comprimento do terreno (m): "))
larg = float(input("Largura do terreno (m): "))

preco = float(input("Preço da tela (R$/m): "))

precoTotal = (comp + larg) * preco

print(f"O custo total para cercar o terreno é de: R${precoTotal:4.2f}")