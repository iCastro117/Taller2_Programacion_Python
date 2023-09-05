# Solicite números ordenados al usuario hasta que el usuario ingrese el símbolo ".".
# Luego calcule la mediana de la lista de la siguiente forma:
# 1) Si la cantidad de números es impar, obtenga el número que se encuentra en la mitad e imprímalo.
# 2) Si la cantidad de números es par, entonces obtenga la pareja de elementos de la mitad e imprima el promedio entre estos dos números.

numeros = []

print("Ingrese los números uno por uno")
print("Para terminar de ingresar los datos, por favor ingrese el símbolo '.' para calcular la mediana.")

while True:
    entrada = input()
    if entrada == ".":
        break

    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada no válida. Ingrese un número válido o '.' para calcular la mediana.")

if not numeros:
    print("No se ingresaron números.")
else:
    def calcular_mediana(numeros):
        numeros.sort()
        n = len(numeros)

        if n % 2 != 0:
            return numeros[n // 2]
        else:
            medio1 = numeros[(n - 1) // 2]
            medio2 = numeros[n // 2]
            return (medio1 + medio2) / 2.0

    mediana = calcular_mediana(numeros)
    print("La mediana es:", mediana)
