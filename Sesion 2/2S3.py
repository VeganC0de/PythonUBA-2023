#Crear un programa que le solicite al usuario un entero y determine si es par, mostrando por pantalla un
#mensaje que indique el resultado.
# Para determinar si un número es par o impar, se puede determinar con el uso del operador %, les
 # dejamos a ustedes el cómo.

num = int(input("Por favor Ingrese un numero y le dire si es par o no : "))

if num%2 == 0:
    print("Su numero es par")
else: print("Su numero no es par")