#Genero un numero aleatorio
import random
numero_aleatorio = random.randint(0, 9)

intentos = 0  #contador de intentos

#Se le solicita al usuario que intente adivinar cuál es el número
adivinar_numero = int (input ("Adivine el número entre 0 y 9: "))

while adivinar_numero != numero_aleatorio:
    if adivinar_numero < 0 or adivinar_numero > 9:
        print ("Se debía ingresar un número entre 0 y 9")
    else: 
        intentos += 1   #Contamos los intentos incorrectos
    adivinar_numero = int (input ("Vuelva a intentar adivinar el número entre 0 y 9: ")) 

#Contamos el intento que fue correcto
intentos += 1

print (f"Ha podido adivinar el número en {intentos} intentos")