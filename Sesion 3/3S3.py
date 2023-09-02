#6. Escribir código que dado dos enteros, determine si la suma de ambos da menos que 100. Si la suma de
#ambos es menor a 100, calcular cuánto falta para llegar a 100 y mostrar por pantalla un mensaje con
#ese valor. Si la suma es mayor a 100, mostrar un mensaje diciendo “Llega a 100”

entero1 = 30
entero2 = 70

if (entero1+entero2>100):
    print("Llega a 100")
else: print("La suma de ambos le falta ",100-(entero1+entero2)," unidades para llegar al 100")


#7. Se tienen letras para representar las estaciones del año:
#● V para verano
#● O para otoño
#● I para invierno
#● P para primavera
#Crear una función que dada una letra, imprima por pantalla la estación del año que representa (es
#decir, si se ingresa V se mostrará por pantalla el mensaje “Verano”). En caso de no representar a
#ninguna estación mostrar un mensaje que diga “error”. Probar la función creada llamándola con A, P, O,
#B, V e I.

letra= 'O'

def estacion(letra):
    if letra=='V':
        print("Verano")
    elif letra=='O':
        print("Otoño")
    elif letra=='I':
        print("Invierno")
    elif letra=='P':
        print("Primavera")
    else:
        print("Ingrese un valor correcto")

estacion(letra)