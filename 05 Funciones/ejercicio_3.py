import utils
# Le pedimos al usuario que ingrese nombre, apellido, edad y residencia y guardamos dichos valores en variables
nombre = input ("Ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")
edad = int (input ("Ingrese su edad: "))
residencia = input ("Ingrese su residencia: ")
# Llamamos a la función para mostrar el resultado
utils.informacion_personal (nombre, apellido, edad, residencia)