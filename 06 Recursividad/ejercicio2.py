# Función recursiva para calcular el n-ésimo número de Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Función para mostrar la serie completa hasta una posición dada
def mostrar_serie_fibonacci(hasta):
    print("Serie de Fibonacci hasta la posición", hasta, ":")
    for i in range(hasta + 1):
        print(fibonacci(i), end=" ")
    print()

# Solicita al usuario una posición
posicion = int(input("Introduce una posición para la serie de Fibonacci: "))

# Muestra la serie
mostrar_serie_fibonacci(posicion)