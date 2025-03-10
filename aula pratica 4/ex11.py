a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
d = float(input("Digite o valor de d: "))
e = float(input("Digite o valor de e: "))
f = float(input("Digite o valor de f: "))

while a != 0 or b != 0 or c != 0 or d != 0 or e != 0 or f != 0:
    if a * e - b * d > 0:

        x = (c * e - b * f) / (a * e) - (c * d)
        y = (a * f - c * d) / (a * e) - (c * d)

        print(f"X = {x:5.2f}, Y = {y:5.2f}")
    else:
        print("O sistema não tem solução!")

    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    d = float(input("Digite o valor de d: "))
    e = float(input("Digite o valor de e: "))
    f = float(input("Digite o valor de f: "))
