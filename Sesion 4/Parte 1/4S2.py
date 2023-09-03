#Ejercicios con listas y tuplas


#8. Se quiere guardar información de los siguientes países: Francia, Argentina, Japón, Alemania, Perú.
#a. Crear una tupla para cada país que contenga su nombre, su capital y el continente donde se encuentra.
#b. Guardar las tuplas en una lista.
#c. Hacer una función que reciba por parámetros la lista, e imprima la información de cada país con el siguiente formato:
#País: <nombre>
#Capital: <capital>
#Continente: <continente>
#Por ejemplo:
#País: Japón
#Capital: Tokio
#Continente: Asia

# a y b
paises = [("Argentina", "Buenos Aires", "LATAM SUR"), 
          ("Francia", "Paris", "Europa"), 
          ("Japon", "Tokyo", "Asia"), 
          ("Alemania", "Berlin", "Europa"), 
          ("Perú", "Lima", "LATAM SUR")]

#c
def infoPaises(paises):
    for pais in paises:
        tierra, capital, continente = pais
        print("PAIS:", tierra)
        print("CAPITAL:", capital)
        print("CONTINENTE:", continente)


infoPaises(paises)

print("-------------------------------------------------------------------------------------------------------------------------")


#9. Una librería tiene un sistema que guarda los nombres de todos los libros que tienen en una lista de la
#siguiente forma: [“El principito”, “It”, “Sherlock Holmes”...]. Se quiere saber cuántos libros repetidos
#tienen. Hacer código que imprima para cada título, cuántos ejemplares hay.
#Aclaración: No se sabe la cantidad de elementos que tiene la lista, la lista nombrada es solo un ejemplo


libros = ["El principito", "It", "Sherlock Holmes", "It", "El principito", "Harry Potter", "Sherlock Holmes"]


contador_libros = {}


for libro in libros:
    if libro in contador_libros:
        contador_libros[libro] += 1
    else:
        contador_libros[libro] = 1


for libro, cantidad in contador_libros.items():
    if cantidad > 1:
        print(f"{libro}: {cantidad} ejemplares")



print("-------------------------------------------------------------------------------------------------------------------------")


#10. Crear una lista que contenga los números del 1 al 10, luego recorrerla y guardar en otra lista esos
# números elevados al cuadrado.

numeros=[1,2,3,4,5,6,7,8,9,10]
lista=[]
for numero in numeros:
  
  lista.append(numero*numero)  
print(lista)


print("-------------------------------------------------------------------------------------------------------------------------")

#11. Se tiene la siguiente lista de palabras: [“entender”, “pueden”, “humanos”, “los”, “que”, “código”,
#“escriben”, ”programadores”, “buenos”, “Los”, “entiende.”, “computadora”, “una”, “que”, “código”,
#“escribe”, “tonto”, “Cualquier”]. Hacer una función que reciba una lista, y devuelva un string uniendo
#las palabras desde el final de la lista hasta el principio con un “ ” (espacio) entre cada una, para formar
#la frase. (ver funciones de listas y strings).

palabras = ["entender.","pueden","humanos","los","que","código","escriben","programadores","buenos","Los","entiende.","computadora","una","que","código","escribe","tonto","Cualquier"]

palabras.reverse()

texto = " ".join(palabras)

print(texto)

print("-------------------------------------------------------------------------------------------------------------------------")

#12. Se quiere hacer un sistema en la facultad para que un alumno pueda ir guardando las materias que va
#haciendo. Para eso, crear una función que le pregunte al usuario la materia que quiere almacenar, e ir
#guardando la información en una lista hasta que ingrese una ‘X’. ¿Qué funciones de listas no permiten
#insertar en una lista?


def meteMateria():
    aprobadas = []
    materia = ""
    
    while materia != "X":
        materia = input("Ingrese la Materia que aprobó (o 'X' para salir): ")
        if materia != "X":
            aprobadas.append(materia)
    
    print("Materias aprobadas:")
    for materia_aprobada in aprobadas:
        print(materia_aprobada)

meteMateria()





