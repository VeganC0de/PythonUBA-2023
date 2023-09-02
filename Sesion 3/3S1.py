#Expresiones
#Para esta sección de los ejercicios, revisar los temas de operadores lógicos y de comparación.
#1. Escribir la expresión para saber si un número es más grande que otro. Guardarla en una variable de tipo
#bool e imprimirla por pantalla para ver su valor.
#2. Repetir el punto anterior pero con la expresión que determina que una letra NO es vocal.
#3. Repetir pero para la expresión que permite saber si un número es par y menor a 10.



##1
num1 = 1
num2=2
vocal=["a","e","i","o","u","A","E","I","O","U","a",]
if num1>num2:
    print("Num1 es mayor que num2")
else:
    print("num2 es mayor que nume1")

letra="e"


## 2
if letra == vocal:
    print("La letra es una vocal")
else:
    print("La letra no es una vocal")

## 3

if num2<10 and num1%2 == 0:
    print("Tu numero es menor que 10 y par")
else: print("Tu numero no es menor que 10 y par")





