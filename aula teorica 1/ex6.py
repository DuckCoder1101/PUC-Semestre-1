comp = float(input("Digite o comprimento da sala (m): "))
larg = float(input("Digite a largura da sala (m): "))

preco = float(input("Digite o preço do carpet (R$/m²): "))

area = comp * larg

totalGasto = area * preco

print(f"O total gasto para forrar o chão de carpet é: R${totalGasto}")