# Se crea diccionario para almacenar alumnos y sus notas
alumnos = {}

# Ingreso de datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno #{i + 1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingresá la nota #{j + 1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

# Calcular y mostrar promedios
print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")