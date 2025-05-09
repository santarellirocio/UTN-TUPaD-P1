#Se le solicita al usuario que ingrese un número entero positivo
numero_positivo = int (input ("Ingrese un número entero positivo: "))

sumatoria = 0  #inicio la variable sumatoria en 0
if numero_positivo <= 0:
    print ("Se debía escribir un número mayor a 0")
else:
    #Suma de todos los números enteros comprendidos entre dos valores dados por el usuario
    for numero in range (numero_positivo+1):
        sumatoria += numero
        #Mostramos por pantalla el resultado de la suma
    print (f"La suma de todos los números enteros comprendidos entre 0 y {numero_positivo} es: {sumatoria}")