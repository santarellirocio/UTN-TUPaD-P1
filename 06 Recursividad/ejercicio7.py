# Función recursiva para contar los bloques necesarios para construir la pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Pruebas
if __name__ == "__main__":
    print(contar_bloques(1))  # → 1
    print(contar_bloques(2))  # → 3
    print(contar_bloques(4))  # → 10