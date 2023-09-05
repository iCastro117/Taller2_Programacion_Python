# Pide al usuario que ingrese varios valores enteros, que pueden ser
# positivos o negativos. Cuando se ingrese un cero, el programa debe terminar y mostrar un
# gráfico de cuántos valores positivos y negativos fueron ingresados (debe imprimir un * por
# cada número positivo y negativo):

contador_positivos = 0
contador_negativos = 0

print("Ingrese números positivos o negativos (ingrese 0 para terminar):")

while True:
    valor = int(input())

    if valor == 0:
        break  # Termina el programa si se ingresa 0

    if valor > 0:
        contador_positivos += 1
    else:
        contador_negativos += 1

print("Gráfico de valores positivos:")
print("*" * contador_positivos)

print("Gráfico de valores negativos:")
print("*" * contador_negativos)