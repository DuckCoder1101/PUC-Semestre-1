valorCompra = float(input("Digite o valor total da compra (R$): "))
valorPago = float(input("Digite o valor pago (R$): "))

trocoTotal = valorPago - valorCompra
troco = valorPago - valorCompra

cedulas = [100, 50, 20, 10, 5, 1]

cedulas100 = 0
cedulas50 = 0
cedulas20 = 0
cedulas10 = 0
cedulas5 = 0
cedulas1 = 0

while troco >= 1:
    for cedula in cedulas:
        if (troco >= cedula):
            troco -= cedula

            if cedula == 100:
                cedulas100 += 1
                break

            elif cedula == 50:
                cedulas50 += 1
                break

            elif cedula == 20:
                cedulas20 += 1
                break

            elif cedula == 10:
                cedulas10 += 1
                break

            elif cedula == 5:
                cedulas5 += 1
                break

            else:
                cedulas1 += 1
                break

if (trocoTotal == 0):
    print("Não há troco!")

else:
    print(f"O troco será de R${trocoTotal}")
    print(f"O valor será distribuido em:")
    print(f"{cedulas100} notas de 100")
    print(f"{cedulas50} notas de 50")
    print(f"{cedulas20} notas de 20")
    print(f"{cedulas10} notas de 10")
    print(f"{cedulas5} notas de 5")
    print(f"{cedulas1} notas de 1")