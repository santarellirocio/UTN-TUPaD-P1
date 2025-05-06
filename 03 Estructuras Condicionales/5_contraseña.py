#Solicitamos al usuario una contraseña
contraseña = str (input("Por favor, ingrese una contraseña de entre 8 y 14 caracteres: "))

#Si el usuario ingresa una contraseña de longitud adecuada, se imprime por pantalla "Ha ingresado una contraseña correcta"
if len (contraseña) >= 8 and len (contraseña) <= 14 :
    print ("Ha ingresado una contraseña correcta")
#Caso contrario, se imprime por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")