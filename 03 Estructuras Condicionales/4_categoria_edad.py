#Solicitamos al usuario su edad
edad = int(input ("Ingrese su edad: "))

#Creo la variable categoria
categoria = ""
#Niño/a: menor de 12 años. 
#Adolescente: mayor o igual que 12 años y menor que 18 años. 
#Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#Adulto/a: mayor o igual que 30 años.
if edad >= 0 and edad < 12:
    categoria = "Niño/a"
elif edad >= 12 and edad < 18:
    categoria = "Adolescente"
elif edad >= 18 and edad < 30:
    categoria = "Adulto/a joven"
elif edad >= 30:
    categoria = "Adulto/a"
else:
    categoria = "El número ingresado no corresponde con una edad válida"
print (categoria)