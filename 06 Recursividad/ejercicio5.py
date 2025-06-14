# Función recursiva para verificar si una palabra es un palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Programa principal
if __name__ == "__main__":
    palabra = input("Ingresa una palabra (sin espacios ni tildes): ").lower()
    if es_palindromo(palabra):
        print(f'"{palabra}" es un palíndromo.')
    else:
        print(f'"{palabra}" no es un palíndromo.')