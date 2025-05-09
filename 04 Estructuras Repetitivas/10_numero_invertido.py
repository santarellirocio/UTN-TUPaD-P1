#Se le solicita al usuario que ingrese un número entero
numero = int (input("Ingresa un número entero: "))

#La variable signo al final le agrega el "-" si el número ingresado era negativo
signo = -1 if numero < 0 else 1 
numero = abs(numero) #tomo el valor absoluto del número

numero_invertido = 0

#Se invierte el orden de los dígitos de un número ingresado por el usuario
while numero > 0:
    digito = numero % 10 #Del resto obtengo el último dígito del número
    numero_invertido = numero_invertido * 10 + digito #Guardo el dígito obtenido
    numero //= 10 #Recorto el número sacandole el último dígito

numero_invertido *= signo #Se le agrega el signo "-" si el número ingresado era negativo
print("El número invertido es:", numero_invertido)