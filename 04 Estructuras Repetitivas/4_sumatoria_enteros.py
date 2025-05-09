#Se le solicita al usuario que ingrese un número entero
numero = int (input ("Ingrese un número entero (0 para detenerse): "))
#Creamos la variable sumatoria
sumatoria = 0
#Se vuelve a pedir al usuario que ingrese otro número entero mientras sea distinto de 0
while numero != 0:
    sumatoria += numero #se suma el número ingresado en la variable sumatoria
    numero = int (input ("Vuelva a ingresar un número entero (0 para detenerse): "))

#Se imprime por pantalla el total acumulado de los números ingresados hasta su interrupción
print (f"El total acumulado de los números ingresados es: {sumatoria}")