#Leer x cantidad de producto comprado a x precio,
#aplica el iva del 15%
#un descuento del 10%
#Mostrar el total antes del IVA
#Monto del IVA
#Monto del descuento
#Total a pagar
"""Se debe leer el nombre de cliente, nombre del producto y mostrar una factura"""
print("="*20)
print("Sistema de Facturación")
print("="*20)
print("Ingresa los siguientes datos")
cliente = input("Nombre del cliente: ")
producto = input("Nombre del prducto: ")
precio = float(input("Precio del producto: "))
cantidad = float(input("Cantidad el producto: "))

total = precio * cantidad
iva = total * 0.15
descuento = total * 0.1
monto = total + iva - descuento 

import os
press_key = input ("Presiona una tecla para continuar....")
os.system("cls || clear ")
print("+"*30)
print("Factura ")
print("+"*30)
print(f"Cliente: {cliente}")
print(f"Productos \t Cantidad \t Precio \t Total")
print(f"{producto:>10} \t {cantidad:>10} \t {precio:>10} \t {total:>10}")
print(f"IVA: {iva}")
print(f"Desc: {descuento}")
print(f"Monto: {monto}")
