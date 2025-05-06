#Se le solicita al usuario que ingrese la magnitud de un terremoto
magnitud_terremoto = float (input ("Ingrese la magnitud de un terremoto: "))

#Se clasifica la magnitud en una de las siguientes categorías según la escala de Richter e imprime el resultado por pantalla:
if magnitud_terremoto < 3:
    print ("Muy leve (imperceptible)")
elif 3 <= magnitud_terremoto < 4:
    print ("Leve (ligeramente perceptible)")
elif 4 <= magnitud_terremoto < 5:
    print ("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud_terremoto < 6:
    print ("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud_terremoto < 7:
    print ("Muy fuerte (puede causar daños significativos)")
elif magnitud_terremoto >= 7:
    print ("Extremo (puede causar graves daños a gran escala)")