# (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
cont = 1 
pares = 0        #Variable que cuenta la cantidad de pares, iniciada en 0.
impares = 0      #Variable que cuenta la cantidad de impares, iniciada en 0.
positivos = 0    #Variable que cuenta la cantidad de positivos, iniciada en 0.
negativos = 0    #Variable que cuenta la cantidad de negativos, iniciada en 0.

#Le pide al usuario ingresar 100 números enteros.
while cont <= 100:
    numero = int (input (f"Ingrese el número entero {cont}: "))
    cont += 1
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero >= 0:
        positivos += 1
    else:
        negativos += 1

#Se muestra por pantalla cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. 
print (f"De los 100 números enteros ingresados, {pares} son pares, {impares} son impares, {positivos} son positivos y {negativos} son negativos.")