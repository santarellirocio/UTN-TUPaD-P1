import math
# Definición de funciones
def imprimir_hola_mundo ():
    print ("Hola Mundo!")

def saludar_usuario (nombre):
    print(f"Hola {nombre}!")

def informacion_personal(nombre, apellido, edad, residencia):
    nombre.lower()
    apellido.lower()
    residencia.lower()
    print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")   

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

def segundos_a_horas(segundos):
    return segundos / 3600

def tabla_multiplicar(numero):
    print(f"La tabla de multiplicar de {numero} es:")
    for i in range (1,11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def operaciones_basicas(a, b):
    suma_a_b = a + b

    print(f"""
  Resultado de la suma: {suma_a_b}
  Resultado de la resta: {a-b}
  Resultado de la división: {a/b}
  Resultado de la multiplicación: {a*b}
      """)

def calcular_imc(peso, altura):
    imc = round(peso / altura**2, 2)
    print(f"Su IMC es de: {imc}")

def celsius_a_fahrenheit(celsius):
    fahrenheit = round((9/5) * celsius + 32, 2)
    print(f"{celsius} °C equivalen a {fahrenheit} °F.")

def calcular_promedio(a, b, c):
    promedio_a_b_c = round((a+b+c)/3, 2)
    print(f"El promedio de los números ingresados es {promedio_a_b_c}.")
