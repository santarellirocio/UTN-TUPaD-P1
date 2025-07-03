# Agenda con eventos predeterminados
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("lunes", "16:00"): "Peluquería",
    ("martes", "15:00"): "Clases de italiano",
    ("miercoles", "14:30"): "Clases de zumba",
    ("viernes", "18:00"): "Trabajo"
}

# Consulta de eventos
print("=== CONSULTA DE AGENDA ===")
dia = input("Ingresá el día (en minúscula, ej: lunes): ").lower()
hora = input("Ingresá la hora (formato HH:MM, ej: 10:00): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad programada: {agenda[clave]}")
else:
    print("No hay ninguna actividad programada en ese horario.")