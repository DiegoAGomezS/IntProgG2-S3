precio_org = float(input("Ingrese el precio original del producto: "))
descuento = float(input("Ingrese el descuento que posee el producto (Preferiblemente en decimal): "))

precio_descuento = precio_org - ((precio_org * descuento) / 100)

IVA = float(input("Ingrese el porcentaje del IVA (En decimal): "))

impuesto = ((precio_descuento * IVA) / 100)
precio_final = precio_descuento + impuesto

print("Usted tenía un producto con un precio de: ", precio_org)
print("Su descuento es del: ", descuento)
print("Aplicándolo su precio pasa a ser: ", precio_descuento)
print("El IVA que posee es: ", impuesto)
print("Por lo tanto su precio final es: ", precio_final)