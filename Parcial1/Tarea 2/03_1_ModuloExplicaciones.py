# Base de conocimientos: Preferencias y actividades recomendadas
preferencias_actividades = {
    "Deportes": ["Correr", "Nadar", "Ciclismo"],
    "Arte": ["Pintar", "Bailar", "Tocar un instrumento"],
    "Viajes": ["Explorar nuevas ciudades", "Hacer senderismo en la naturaleza", "Probar comidas locales"]
}

# Función para recomendar actividades basadas en preferencias
def recomendar_actividades(preferencias):
    explicaciones = []
    actividades_recomendadas = []
    for preferencia, actividades in preferencias_actividades.items():
        if preferencia in preferencias:
            actividades_recomendadas.extend(actividades)
            explicaciones.append(f"Basado en tu preferencia por {preferencia}, te recomendamos las siguientes actividades: {', '.join(actividades)}")
    return actividades_recomendadas, explicaciones

# Preferencias del usuario
preferencias_usuario = ["Deportes", "Viajes"]

# Recomendar actividades
actividades_recomendadas, explicaciones = recomendar_actividades(preferencias_usuario)

# Imprimir actividades recomendadas
print("Actividades recomendadas:", actividades_recomendadas)

# Imprimir explicaciones
print("\nExplicaciones:")
for explicacion in explicaciones:
    print(explicacion)
