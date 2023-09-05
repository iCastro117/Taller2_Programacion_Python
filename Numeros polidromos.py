# Una función para verificar si una cadena es un palíndromo
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
cadena = input()

if es_palindromo(cadena):
    print(cadena + " es palíndromo.")
else:
    print(cadena + " no es palíndromo.")