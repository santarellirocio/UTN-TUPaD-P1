import utils
# Le pedimos al usuario que ingrese 2 números, donde el segundo debe ser distinto de cero ya que no se puede dividir un número por 0
num_a = float(input("Por favor, ingrese un número: "))
num_b = float(input("Por favor, ingrese otro número distinto de 0: "))
# Ponemos la condición en caso de que ingrese el 0 como segundo número
if num_b == 0:
    print ("ERROR. Por favor, ingrese un número distinto de 0: ")
else:
    utils.operaciones_basicas(num_a, num_b)  # Llamamos a la función para mostrar el resultado de las operaciones entre dichos valores