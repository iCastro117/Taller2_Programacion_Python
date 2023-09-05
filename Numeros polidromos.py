# Un número natural es un palíndromo si se lee igual de izquierda a derecha y de derecha a izquierda.
# Por ejemplo, 14941 es un palíndromo, mientras que 81924 no lo es.
# Escriba un programa que indique si el número ingresado es o no palíndromo:

# Importar la librería para leer entrada del usuario
import sys

def es_palindromo(cadena):
    # Eliminar espacios y convertir a minúsculas
    cadena = cadena.replace(" ", "").lower()

    longitud = len(cadena)

    for i in range(longitud // 2):
        if cadena[i] != cadena[longitud - i - 1]:
            return False

    return True

# Programa principal
print("Ingrese un número: ")
cadena = sys.stdin.readline().strip()  # Leer la entrada y eliminar el salto de línea

if es_palindromo(cadena):
    print(cadena + " es palíndromo.")
else:
    print(cadena + " no es palíndromo.")
