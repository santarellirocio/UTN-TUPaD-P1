# Función recursiva para calcular el factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Programa principal
def mostrar_factoriales(hasta):
    for i in range(1, hasta + 1):
        print(f"Factorial de {i} es {factorial(i)}")

# Bloque principal con entrada del usuario
if __name__ == "__main__":

    numero = int(input("Ingresa un número entero positivo: "))
    if numero < 1:
        print("Por favor, ingresa un número mayor o igual a 1.")
    else:
        mostrar_factoriales(numero)