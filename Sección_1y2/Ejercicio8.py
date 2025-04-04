dolares = float(input("Ingrese los dolares que tiene a disposición: "))

tasa_euro = 0.92
tasa_libras = 0.78
tasa_yenes = 150.25

cantidad_euros = dolares * tasa_euro
cantidad_libras = dolares * tasa_libras
cantidad_yenes = dolares * tasa_yenes

print("Usted ingreso una cantidad de", dolares, "Dolares")
print(f'El equivalente en Euros es: {cantidad_euros:.2f}')
print(f'El equivalente en Libras es: {cantidad_libras:.2f}')
print(f'El equivalente en Yenes es: {cantidad_yenes:.2f}')