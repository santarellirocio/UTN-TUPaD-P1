# Solicitar una frase al usuario
frase = input("Ingresá una frase: ")

# Separar la frase en palabras
palabras = frase.split()

# Obtener palabras únicas
palabras_unicas = set(palabras)

# Contar frecuencia de cada palabra
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

# Mostrar resultados
print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)