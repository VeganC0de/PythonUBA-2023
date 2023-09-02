#8. Se quiere hacer un programa para enseñar a unos niños a contar. Crear una función que reciba un
#número entero e imprima por pantalla los números del 1 hasta ese número con la estructura de control
#iterativa for.
#9. Se quiere mejorar el programa para enseñar matemáticas pensado en el ejercicio anterior. Ahora se
#necesita una funcionalidad que permita a los niños aprender las tablas. Crear una función que reciba un
#número entero e imprima por pantalla la tabla de ese número del 1 al 10.
#10. Crear una función que simule un cumpleaños: que dado un entero imprima “Que los cumplas feliz” esa
#cantidad de veces.

#8
num = 15

for i in range(0,num):
    print(i+1)

print("----------------------------------------------------------")
#9

def tablas(num):
    for i in range(0,11):
        print(i*num)

tablas(num)


#10

cantidad = 4

for i in range(0,cantidad):
    print("Que lo cumplas feliz")

