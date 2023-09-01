#5. Crear un programa que le solicite al usuario 5 enteros y muestre por pantalla el promedio de ellos.
#Es muy común usar variables para acumular valores.


acumulador = 0



num= int(input("Por favor ingrese un numero entero : " ))
acumulador = acumulador + num
num= int(input("Por favor ingrese un numero entero : " ))
acumulador = acumulador + num
num= int(input("Por favor ingrese un numero entero : " ))
acumulador = acumulador + num
num= int(input("Por favor ingrese un numero entero : " ))
acumulador = acumulador + num
num= int(input("Por favor ingrese un numero entero : " ))
acumulador = acumulador + num
     

promedio = acumulador / 5


print("El promedio de los numero introducidos es de: ", promedio)