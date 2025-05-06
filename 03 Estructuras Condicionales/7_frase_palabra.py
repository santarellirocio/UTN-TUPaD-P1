#Se le solicita al usuario una frase o palabra
frase_palabra = input("Por favor, ingrese una frase o palabra: ")

#Si el string ingresado termina con vocal se añade un signo de exclamación al final y se imprime el string resultante por pantalla
if frase_palabra[-1].lower() in "aeiou":
    print ((frase_palabra + "!"))
#Caso contrario, deja el string tal cual lo ingresó el usuario y se imprime por pantalla
else:
    print (frase_palabra)