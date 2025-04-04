peso_kg = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Proporcione su altura: "))

altura_2 = altura * altura
IMC = peso_kg / altura_2

Estandar01 = IMC * 100
Estandar02 = Estandar01 / 100


print ("Peso ingresado: ", peso_kg)
print ("Altura ingresada: ", altura)
print ("IMC calculado: ", IMC)
print ("IMC estándar: ", round(Estandar02, 2))

if Estandar02 < 18.5:
    clasificacion = "Bajo peso"
elif 18.5 <= IMC < 24.9:
    clasificacion = "Peso normal"
elif 25 <= IMC < 29.9:
    clasificacion = "Sobrepeso"
else:
    clasificacion = "Obesidad"

print("Clasificación:", clasificacion)