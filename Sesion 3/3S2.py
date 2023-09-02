#4. Crear una función que dado un número, devuelva su valor absoluto. El valor absoluto de un número es
#el mismo número sin considerar el signo.
#Por ejemplo, el absoluto de 2 es 2 (|2| = 2) y el absoluto de -4 es 4 (|-4|=4).
#5. Crear el programa al que sea imposible ganarle en el juego de “Piedra, papel o tijera”. Cada elemento va
# ser representado con una letra: R para piedra, P para papel y T para tijera.
#a. Hacer una función que le haga al usuario ingresar alguna de esas letras, e imprima por pantalla
#la jugada para ganarle. Por ejemplo:
#> ¡Juguemos! Ingresá piedra ( R), papel (P) o tijera (T)
#> P
#> Tijera. ¡Te gané!
#ATENCIÓN: Observar cómo se usa una frase inicial para darle a entender al usuario lo que tiene
#que hacer (en este caso ingresar alguna de las tres letras).
#b. Mostrar por pantalla el mensaje “NO vale” cuando el usuario ingresa una letra no válida
#(distinta de R, P o T).

#4
def absoluto(numero):
    if numero<0:
        numero = numero * -1
    print("El absoluto de tu numero es :  ",numero)  

digito=-5
absoluto(digito)


#5

def juguemos():
    print("Juguemos! Ingresá piedra (R),papel(P) o tijeras(T)")
    jugada = input()

    if (jugada == 'R' or jugada == 'T' or jugada == 'P') :
        if(jugada == 'P'):
            print( "Tijeras!, gane!")
        elif(jugada == 'R'):
            print( "Papel!, gane!")
        elif(jugada == 'T'):
            print("Piedra!, gane!")

    else:
        print("Ingrese una letra correcta")

juguemos()