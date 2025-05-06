#Se le solicita al usuario que ingrese su nombre
nombre = input ("Ingrese su nombre: ")

#Se le solicita al usuario que seleccione el número 1, 2 o 3 dependiendo de la opción que desee:
print("Seleccione la opción 1, 2 o 3 según lo que desee:")
print("1. Si quiere su nombre en mayúsculas.")
print("2. Si quiere su nombre en minúsculas.")
print("3. Si quiere su nombre con la primera letra mayúscula.")
opcion = input("Elegí una opción (1-3): ")
if  opcion == "1":
    print (nombre.upper())
elif opcion == "2":
    print (nombre.lower())
elif opcion == "3":
    print (nombre.title())
else:
    print ("Por favor seleccione opción 1, 2 o 3")