total = float(input("Digite o valor total (R$): "))

primeiro = total * .46
segundo = total * .32

total -= primeiro + segundo

print(f"O 1° irá receber R${primeiro}, o 2° R${segundo} e o terceiro R${total}")