#Se le solicita al usuario un número entero
numero_entero = int (input ("Por favor, ingrese un número entero: "))
#Tomamos el valor absoluto del número
numero_entero = abs (numero_entero)

if numero_entero == 0:
    cantidad_digitos = 1
else:
    cantidad_digitos = 0
    while numero_entero > 0:
        numero_entero = numero_entero // 10
        cantidad_digitos += 1

#Se imprime por pantalla la cantidad de dígitos que tiene el número
print (f"El número ingresado tiene {cantidad_digitos} dígitos")