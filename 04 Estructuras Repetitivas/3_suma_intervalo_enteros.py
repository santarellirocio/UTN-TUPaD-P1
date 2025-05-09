#Se le solicita al usuario que ingrese dos números enteros
numero_inicial = int (input ("Ingrese el primer número entero: "))
numero_final = int (input ("Ingrese el segundo número entero: "))
#Si el número inicial es mayor al número final, si invierte las posiciones
if numero_inicial > numero_final:
    numero_inicial , numero_final = numero_final , numero_inicial

sumatoria = 0
#Suma de todos los números enteros comprendidos entre dos valores dados por el usuario
for numero in range (numero_inicial+1,numero_final):
    sumatoria += numero

#Mostramos por pantalla el resultado de la suma
print (f"La suma de todos los números enteros comprendidos entre {numero_inicial} y {numero_final} es: {sumatoria}")