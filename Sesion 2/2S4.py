#4. Escribir un programa que le pida a un usuario su año de nacimiento y otro año, y le diga qué edad tenía
#el usuario en el año ingresado.

anio = int(input( "Por favor, ingrese el año de su nacimiento: "))

aniores = int(input( "Por favor ingrese otro año para averiguar cuantos años tenia en el mismo : "))

respuesta = aniores - anio

print("En el año ",aniores," usted tenia :", respuesta)

