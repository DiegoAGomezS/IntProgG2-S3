temp_fah = float(input("Ingresa la temperatura en F: "))
temp_Cel =  ((temp_fah - 32) * 5)/9
temp_kel = temp_Cel + 273.15

print (f'Grados Celsius: {temp_Cel:.2f}')
print (f'Grados Kelvin: {temp_kel:.2f}')