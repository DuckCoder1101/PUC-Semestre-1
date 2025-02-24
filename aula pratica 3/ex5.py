alturaDegrau = float(input("Digite a altura do degrau (cm): "));
alturaTotal = float(input("Digite a altura total (m): "))

alturaCm = alturaTotal * 100

sobra = alturaCm % alturaDegrau
degrais = int(alturaCm / alturaDegrau)

print(f"A quantidade de degrais necessários é {degrais}, com uma margem de {sobra:2.2}cm.")