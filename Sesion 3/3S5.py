#11. En un almacén están buscando la forma de hacer los cobros más automáticamente. Para esto, se nos
#pide crear una función que reciba un número entero que representa lo que hay que cobrar, le pida al
#usuario ingresar un monto, y se vaya mostrando por pantalla cuánto falta para completar el pago.
#Repetir este proceso hasta que la deuda sea 0 o menor. Por ejemplo, si se recibe el monto 30:
#> El importe a pagar es de 30 pesos. Por favor, ingrese un monto.
#> 10
#> El importe a pagar es de 20 pesos. Por favor, ingrese un monto.
#> 15
#> El importe a pagar es de 5 pesos. Por favor, ingrese un monto.
#> 5



def cobrar(monto):
    while monto > 0:
        pago = float(input("El importe a pagar es de {}. Por favor ingrese un monto: ".format(monto)))
        if pago <= 0:
            print("El monto ingresado debe ser mayor que cero.")
        elif pago > monto:
            print("El monto ingresado es mayor que el importe restante.")
        else:
            monto -= pago

    if monto <= 0:
        print("El monto se ha pagado en su totalidad")








    

