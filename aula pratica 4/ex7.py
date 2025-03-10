salario = float(input("Digite o seu salário atual: "))
plano = int(input("Digite o plano de salário (1, 2 ou 3): "))

if plano == 1:
    salario *= 1.10
elif plano == 2:
    salario *= 1.15
else:
    salario *= 1.2

print(f"O seu novo salário será {salario:5.2f}")