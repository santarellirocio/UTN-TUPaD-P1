#Programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores.
cont = 1 
sumatoria = 0

# Se le pide al usuario ingresar 100 números enteros.
while cont <= 100:
    numero = int (input (f"Ingrese el número entero {cont}: "))
    cont += 1
    sumatoria += numero

#Calculo la media de los 100 números enteros ingresados por el usuario
media = sumatoria / 100

#Muestro por pantalla la media de los 100 números ingresados
print (f"La media de los 100 números ingresados es: {media}")