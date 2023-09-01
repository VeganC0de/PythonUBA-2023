#7. Crear una función que una un string y un entero, ambos dentro de un string.

palabra=str("numero")
num=int(9)


def unir(vocablo,cifra):
    enterostr=str(cifra)
    resultado = vocablo +" " + enterostr
    print(resultado)

unir(palabra,num)