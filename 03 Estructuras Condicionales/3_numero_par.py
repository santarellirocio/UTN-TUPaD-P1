#Solicitamos al usuario que ingrese un número par
numero = int(input ("Ingrese un número par: "))

#Si el número es divisible por 2 imprime por pantalla "Ha ingresado un número par"
if numero % 2 == 0:
    print ("Ha ingresado un número par")
#Si el número no es divisible por 2 imprime por pantalla "Por favor, ingrese un número par"
else:
    print ("Por favor, ingrese un número par")