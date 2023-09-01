#12. Obtener una palabra, borrarle todas las ‘a’ e imprimirla por pantalla (pista: usar una función predefinida de Python).


palabra = input("Ingrese una palabra: ")

palabra_sin_a = palabra.replace('a', '')

print("La palabra sin 'a' es:", palabra_sin_a)