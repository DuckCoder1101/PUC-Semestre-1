dolares = float(input("Digite um valor em dolares: "))
cotacao = float(input("Digite a cotação do dolar: "))

reais = dolares * cotacao

print(f"O valor na cotação atual equivale a: R${reais:<10.2f}")