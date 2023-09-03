#Familiarización con secuencias
#1. Crear una lista con los números del 1 al 10. Acceder con el índice a la posición que contiene el número
#5, e imprimirlo por pantalla. Recordar que el índice de las listas empiezan con 0.

numeros=[1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
    print(numero)

#prueba con asignacion de variables

numero = numeros[2]

print(numero)

print("-------------------------------------------------------------------------------------------------------------------------")

#2. Con la lista del punto anterior, usar la función len() para averiguar su longitud, e imprimirla.

print("La lista numeros tiene: ",len(numeros), " numeros adentro")

print("-------------------------------------------------------------------------------------------------------------------------")

#3. Crear una secuencia con números distintos, y luego devolver el elemento máximo y el mínimo

desordenados = [45,90,2,33,9,120]

max_valor = desordenados[0]
min_valor = desordenados[0]

#Probando con un for
for numero in desordenados:
    if numero > max_valor:
        max_valor = numero
    elif numero < min_valor:
        min_valor = numero

print("El maximo sacado con FOR es: ",max_valor,"Y el minimo es: ",min_valor)

#Probando con la funcion .max y .mix

maximo= max(desordenados)
minimo = min(desordenados)

print("El maximo es: ",maximo,"Y el minimo es: ",minimo)

print("-------------------------------------------------------------------------------------------------------------------------")

#4. Ordenar la secuencia del ejercicio anterior, e imprimirla por pantalla. (ver funciones de listas)

ordenados = sorted(desordenados)

print("Lista ordenada ascendente: ", ordenados)

print("-------------------------------------------------------------------------------------------------------------------------")

#5. Crear una tupla que guarde tu nombre y tu edad. Luego, imprimir por pantalla tu edad, accediendo al elemento de la tupla que corresponda.

miNombre = ("Daniel","22")

nombre,edad = miNombre

print("Hola mi nombre es: ", nombre, " y mi edad es: ", edad)

print("-------------------------------------------------------------------------------------------------------------------------")

#6. Hacer una lista con 5 nombres, y realizar las siguientes actividades con la misma:
#a. Cambiar el último elemento de la lista y cambiar el último nombre por “Juan”. Olvidándonos de
#que sabemos que tiene 5 elementos, ¿Cómo podría saber cuál es el último elemento si no sé la
#longitud?
#b. Devolver el nombre que esté a dos posiciones del final. ¿Cómo hacemos para que nos funcione
#para cualquier lista y no solo para la que tenga 5 elementos?
#c. Recorrer la lista e imprimir cada nombre por pantalla.
#d. Imprimir por pantalla la lista con 3 repeticiones, usar el operador repetición (*).

#a
registro = ["Daniel","John","Clara","Pablo","Renata"]

longitud = len(registro)

registro.remove(registro[longitud-1])
registro.append("Juan")

#b
print(registro[longitud-3])

#c
for nombre in registro:
    print(nombre)

#d
for nombre in registro:
    print(nombre*3)

print("-------------------------------------------------------------------------------------------------------------------------")

#7. Se pide ahora crear 3 tuplas como las del ejercicio 5, con un nombre y una edad. A continuación,
#guardarlas en una lista. Pensar, ¿De que nos servirá guardar las tuplas en una lista en vez de tenerlas
#por separado?

lista0 = []

tupla1 = ("Daniel","22")
tupla2 = ("Maria","52")
tupla3 = ("Candela","26")

lista0.append(tupla1)
lista0.append(tupla2)
lista0.append(tupla3)

print(lista0)


        



