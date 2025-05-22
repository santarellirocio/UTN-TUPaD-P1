import utils
# Le pedimos al usuario que ingrese su peso y su altura y almacenamos sus respuestas en variables de tipo float
peso = float(input("Por favor, ingrese su peso en kilogramos: "))
altura = float(input("Por favor, ingrese su altura en metros: "))
#Llamamos a la función para mostrar el resultado con dos decimales
utils.calcular_imc(peso, altura)