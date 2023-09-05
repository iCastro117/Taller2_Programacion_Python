# Un viajero desea saber cuánto tiempo tomó un viaje que realizó.
# Él tiene la duración en minutos de cada uno de los tramos del viaje.
# Desarrolle un programa que permita ingresar los tiempos de viaje de los tramos y entregue
# como resultado el tiempo total de viaje en formato horas:minutos.
# El programa deja de pedir tiempos de viaje cuando se ingresa un 0.

horas = 0
total_horas_minutos = 0

print("Ingrese el tiempo total del viaje realizado (MINUTOS)")

while True:
    minutos = int(input())
    
    if minutos == 0:
        break  # Salir del bucle si el usuario ingresa 0
    
    # Sumar los minutos ingresados al total
    total_horas_minutos += minutos

# Operaciones
horas = total_horas_minutos // 60
total_horas_minutos %= 60

print(f"Tiempo total de viaje: {horas}:{total_horas_minutos} horas")
