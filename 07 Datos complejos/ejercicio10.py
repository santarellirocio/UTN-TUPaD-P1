# Diccionario original de países y capitales
original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Brasil": "Brasilia", "Uruguay": "Montevideo"}

invertido = {}

for pais in original:
    capital = original[pais]
    invertido[capital] = pais

print (original)
print (invertido)