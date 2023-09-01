#8. Crear una función que reciba un entero y que retorne (devuelva) el resto y el cociente.

num = 4
div = 2

def restoCociente(digito,divi):
    resto=digito%divi
    print("El resto de ", digito,"/",divi,"es :", resto )
    print("Su divisor es: ",divi)

restoCociente(num,div)