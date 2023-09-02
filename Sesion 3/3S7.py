#14. Crear una función que reciba un número entero e imprima los números primos entre 0 y el número
#ingresado.
#AYUDA: un número es primo cuando solamente es divisible por sí mismo y por 1, es decir que para ver
#si es primo hay que ver que el módulo (%) de ese número con los anteriores hasta el 1 (sin incluirlo) sea
#distinto de 0, o sea que no sea divisible.

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def imprimir_primos_hasta(numero):
    for n in range(2, numero + 1):
        if es_primo(n):
            print(n, end=" ")

numero_ingresado = int(input("Ingrese un número entero: "))
print("Números primos entre 0 y", numero_ingresado, ":")
imprimir_primos_hasta(numero_ingresado)