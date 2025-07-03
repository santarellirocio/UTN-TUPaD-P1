# Crear diccionario vacío
contactos = {}

# Cargar 5 contactos
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto #{i + 1}: ")
    numero = input(f"Ingresá el número de teléfono de {nombre}: ")
    contactos[nombre] = numero

# Consultar un contacto
consulta = input("Ingresá el nombre del contacto que querés consultar: ")

if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print("Ese contacto no está en la agenda.")