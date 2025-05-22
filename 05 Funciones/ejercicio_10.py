import utils
# Le pedimos al usuario que ingrese 3 números
num_a = float(input("Por favor, ingrese el primer número: "))
num_b = float(input("Por favor, ingrese el segundo número: "))
num_c = float(input("Por favor, ingrese el tercer número: "))

# Llamamos a la función para mostrar el resultado del promedio de los 3 números
utils.calcular_promedio(num_a, num_b, num_c)