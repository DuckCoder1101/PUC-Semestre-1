autonomia = 12 # Km/L

tempo = int(input("Digite o tempo gasto na viagem (h): "))
vMedia = int(input("Digite a velocidade média (Km/h): "))

distancia = vMedia * tempo # Km
consumo = distancia / autonomia

print(f"O consumo total de combustível é: {consumo:3.2f}L")
print(f"Velocidade média: {vMedia:4.2f}km/h")
print(f"Distância total: {distancia:6.2f}km")
print(f"Tempo gasto: {tempo:4.2f}h")