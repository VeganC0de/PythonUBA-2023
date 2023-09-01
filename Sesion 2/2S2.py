#2. Crear un programa que le solicite al usuario dos números enteros y luego imprima por pantalla:
#● la suma de ambos números
#● la resta de ambos números
#● la multiplicación de ambos números
#● la división entera de ambos números
#● el resto

num1 = int(input("ingrese su primer num"))
num2 = int(input("ingrese su segundo num"))

suma= num1 + num2
resta = num1 - num2
multi = num1 *num2
div= int(num1 / num2)
resto= num1 % num2


print("la suma es : " , suma)
print("la resta es: ",  resta)
print("la div es: ",  div)
print('el resto:' , resto)