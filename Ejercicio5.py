seg = float(input("Ingrese la cantidad de segundos transcurridos: "))

seg_horas = seg / 3600
horas = int(seg_horas)

hora_minutos = (seg - (horas * 3600))/60
minutos = int(hora_minutos)

seg_restantes = seg - (horas * 3600) - (minutos * 60)

print(f"Tiempo convertido: {horas} horas, {minutos} minutos y {seg_restantes:.0f} segundos")