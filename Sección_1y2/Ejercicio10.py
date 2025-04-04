radio =float(input("Por favor ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

area_base = 3.1416 * (radio * radio)
volumen = area_base * altura
area_lateral = ((2 * 3.1416) * (radio * altura))
area_total = area_lateral + (2 * area_base)

print("Radio ingresado: ", radio)
print("Altura ingresada: ", altura)
print(f"Volumen del cilindro: {volumen:.2f}")
print(f"Area totál del cilindro: {area_total:.2f}")