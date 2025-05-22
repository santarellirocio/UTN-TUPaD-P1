import utils
# Le pedimos al usuario que ingrese el valor en segundos a convertir
segundos = int(input("Ingrese la cantidad de segundos que desea obtener su equivalente en horas: "))
# Llamamos a la función para mostrar el resultado de segundos a horas
print (f"{segundos} segundos equivale a {utils.segundos_a_horas (segundos)} horas.")