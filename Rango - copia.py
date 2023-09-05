# En estadística descriptiva, se define el rango de un conjunto de datos reales como la
# diferencia entre el mayor y el menor de los datos.
# Por ejemplo, si los datos son:
# [5.96, 6.74, 7.43, 4.99, 7.20, 0.56, 2.80],
# entonces el rango es 7.43 - 0.56 = 6.87.
# Escriba un programa que:
# - pregunte al usuario cuántos datos serán ingresados,
# - pida al usuario ingresar los datos uno por uno, y
# - entregue como resultado el rango de los datos.
# Suponga que todos los datos ingresados son válidos

def calcular_rango(datos):
    if len(datos) == 0:
        # Si no hay datos, el rango es 0
        return 0
    else:
        # Encontrar el valor máximo y mínimo en la lista
        maximo = datos[0]
        minimo = datos[0]

        for dato in datos:
            if dato > maximo:
                maximo = dato
            if dato < minimo:
                minimo = dato

        return maximo - minimo

# Programa principal
print("Ingrese la cantidad de datos: ")
cantidad_datos = int(input())

datos = []

for i in range(cantidad_datos):
    print(f"Ingrese el dato #{i + 1}: ")
    dato = float(input())
    datos.append(dato)

rango = calcular_rango(datos)

print(f"El rango de los datos es: {rango}")
