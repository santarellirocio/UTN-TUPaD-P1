#Solicitamos al usuario su edad
edad = int(input ("Ingrese su edad: "))

#Dependiendo de la edad ingresada imprimirá a que categoría corresponde
if edad >= 0 and edad < 12:
    print ("Eres un niño/a")
elif edad >= 12 and edad < 18:
    print ("Eres un adolescente")
elif edad >= 18 and edad < 30:
    print ("Eres un/a adulto/a joven")
elif edad >= 30:
    print ("Eres un/a adulto/a")
else:
    print ("El número ingresado no corresponde con una edad válida")