x = int(input("Digite um valor x: "))
n = int(input("Digite um valor n: "))

while n < 0:
    print("n deve ser > 0")
    n = int(input("Digite um valor n: "))

i = 1
while i < n:
    x *= x
    i += 1

print(f"x ^ n é: {x}.")