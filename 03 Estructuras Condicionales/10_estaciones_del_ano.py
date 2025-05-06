#Se le pregunta al usuario en cuál hemisferio se encuentra (N/S)
hemisferio = input ("Ingrese en que hemisferio se encuentra (N/S): ")
hemisferio.lower()
#Se le pregunta al usuario que mes del año es.
mes = input ("¿Que mes del año es?: ")
mes.lower()
#Se le pregunta al usuario que día del año es.
dia = int (input ("¿Que día es?: "))

#Se imprime por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano si se encuentra en el hemisferio norte
if hemisferio == "n": #hemisferio norte
    if (mes == "diciembre" and dia >= 21) or (mes == "enero" or mes == "febrero") or (mes == "marzo" and dia <= 20):
        print ("Se encuentra en invierno")
    elif (mes == "marzo" and dia >= 21) or (mes == "abril" or mes == "mayo") or (mes == "junio" and dia <= 20):
        print ("Se encuentra en primavera")
    elif (mes == "junio" and dia >= 21) or (mes == "julio" or mes == "agosto") or (mes == "septiembre" and dia <= 20):
        print ("Se encuentra en verano")
    elif (mes == "septiembre" and dia >= 21) or (mes == "octubre" or mes == "noviembre") or (mes == "diciembre" and dia <= 20):
        print ("Se encuentra en otoño")
    else:
        print ("La fecha ingresada es incorrecta")
#Se imprime por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano si se encuentra en el hemisferio sur
elif hemisferio == "s": #hemisferio sur
    if (mes == "diciembre" and dia >= 21) or (mes == "enero" or mes == "febrero") or (mes == "marzo" and dia <= 20):
        print ("Se encuentra en verano")
    elif (mes == "marzo" and dia >= 21) or (mes == "abril" or mes == "mayo") or (mes == "junio" and dia <= 20):
        print ("Se encuentra en otoño")
    elif (mes == "junio" and dia >= 21) or (mes == "julio" or mes == "agosto") or (mes == "septiembre" and dia <= 20):
        print ("Se encuentra en invierno")
    elif (mes == "septiembre" and dia >= 21) or (mes == "octubre" or mes == "noviembre") or (mes == "diciembre" and dia <= 20):
        print ("Se encuentra en primavera")
    else:
        print ("La fecha ingresada es incorrecta")
else:
    print ("El hemisferio ingresado es inválido, seleccione N para norte y S para sur")