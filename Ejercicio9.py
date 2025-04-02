duracion_pelicula = float(input("Ingrese la duración de la película en minutos: "))
duracion_comerciales_previos = float(input("Ingrese la duración de los comerciales previos en minutos: "))
cantidad_pausas = int(input("Ingrese la cantidad de pausas comerciales durante la película: "))
duracion_pausa = float(input("Ingrese la duración de cada pausa comercial en minutos: "))

total_comerciales = cantidad_pausas * duracion_pausa

tiempo_total = duracion_pelicula + duracion_comerciales_previos + total_comerciales

print("La duración total de la pelicula es: ", duracion_pelicula)
print("La duración de todos los comerciales en conjunto es", total_comerciales)
print("La duración total de la película con comerciales es: ", tiempo_total, "minutos")