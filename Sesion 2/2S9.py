#9. Pedirle nombre y apellido por separado e imprimir “Apellido, Nombre”.Este proceso se llama concatenar cadenas

nombre=str(input("Ingrese su nombre: "))
apellido=str(input("Ingrese su apellido: "))

nombreApe = nombre + " " + apellido

print("Usted se llama: ", nombreApe)