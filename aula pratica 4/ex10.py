n = int(input("Digite o número de repetições: "))

soma = 0
impares = 0

i = 0
while i < n:
    num = int(input("Digite um número: "))

    if num % 2 == 0:
        soma += num
    else:
        impares += 1

print(f"A soma dos números pares é {soma}")
print(f"O total dos números ímpares é {impares}")