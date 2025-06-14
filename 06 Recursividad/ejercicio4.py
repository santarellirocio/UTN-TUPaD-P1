# Función recursiva que convierte un número decimal positivo a binario como cadena de texto
def decimal_a_binario(n):
    if n < 2:
        return str(n)
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Programa principal
if __name__ == "__main__":

    numero = int(input("Ingresa un número entero positivo en base decimal: "))
    if numero < 0:
        print("Por favor, ingresa un número positivo.")
    else:
        binario = decimal_a_binario(numero)
        print(f"{numero} en binario es: {binario}")