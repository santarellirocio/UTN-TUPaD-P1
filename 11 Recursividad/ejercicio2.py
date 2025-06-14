# Función recursiva para calcular la potencia usando la fórmula n^m = n * n^(m-1)
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Programa principal
if __name__ == "__main__":

    base = float(input("Ingresa la base (número real): "))
    exponente = int(input("Ingresa el exponente (entero no negativo): "))
    
    if exponente < 0:
        print("El exponente debe ser un número entero no negativo.")
    else:
        resultado = potencia(base, exponente)
        print(f"\nResultado: {base}^{exponente} = {resultado}")