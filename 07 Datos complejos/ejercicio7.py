# Ingresar estudiantes que aprobaron el Parcial 1
p1 = input("Ingresá los nombres de los estudiantes que aprobaron el Parcial 1 (separados por coma): ")
parcial1 = set(p1.split(","))

# Ingresar estudiantes que aprobaron el Parcial 2
p2 = input("Ingresá los nombres de los estudiantes que aprobaron el Parcial 2 (separados por coma): ")
parcial2 = set(p2.split(","))

# Eliminar espacios extra
parcial1 = {nombre.strip() for nombre in parcial1}
parcial2 = {nombre.strip() for nombre in parcial2}

# Estudiantes que aprobaron ambos parciales
ambos = parcial1 & parcial2

# Estudiantes que aprobaron solo uno de los dos
solo_uno = parcial1 ^ parcial2

# Estudiantes que aprobaron al menos un parcial
al_menos_uno = parcial1 | parcial2

# Mostrar resultados
print("\nAprobaron ambos parciales:", ambos)
print("Aprobaron solo uno de los dos:", solo_uno)
print("Aprobaron al menos un parcial:", al_menos_uno)