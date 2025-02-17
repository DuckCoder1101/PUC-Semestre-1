salarioAtual = float(input("Digite o seu salário (R$)"))
percentual = float(input("Digite o percentual de reajuste (%): "))

salarioNovo = salarioAtual + (salarioAtual * percentual / 100)

print(f"Salário reajustado: R${salarioNovo}")