# Función recursiva para contar cuántas veces aparece un dígito en un número
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        ultimo = numero % 10
        return (1 if ultimo == digito else 0) + contar_digito(numero // 10, digito)

# Pruebas
if __name__ == "__main__":
    print(contar_digito(12233421, 2))  # → 3
    print(contar_digito(5555, 5))      # → 4
    print(contar_digito(123456, 7))    # → 0