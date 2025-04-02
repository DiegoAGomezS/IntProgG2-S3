print ("Si desee saber las horas totales de su viaje por favor realice lo siguiente:")

tramo1 = float(input("Duración del primer tramo (en horas): "))
escala1 = float(input("Duración de la primera escala (en horas): "))
    
tramo2 = float(input("Duración del segundo tramo (En horas):" ))
escala2 = float(input("Duración de la segunda escala (en horas): "))
    
tramo3 = float(input("Duración del tercer tramo (en horas): "))
     
total = ((tramo1 + escala1) + (tramo2 + escala2)) + tramo3
print(f"El tiempo total del viaje es {total} horas")