#La base de conocimientos preferencias_actividades contiene diferentes categorías de preferencias y actividades asociadas con cada una.
#La función recomendar_actividades recibe las preferencias del usuario y devuelve una lista de actividades recomendadas basadas en esas preferencias.
#Se proporcionan las preferencias del usuario en la lista preferencias_usuario.
#El programa imprime las actividades recomendadas basadas en las preferencias del usuario.


# Base de conocimientos: Preferencias y actividades recomendadas
preferencias_actividades = {
    "Deportes": ["Correr", "Nadar", "Ciclismo"],
    "Arte": ["Pintar", "Bailar", "Tocar un instrumento"],
    "Viajes": ["Explorar nuevas ciudades", "Hacer senderismo en la naturaleza", "Probar comidas locales"]
}

# Función para recomendar actividades basadas en preferencias
def recomendar_actividades(preferencias):
    actividades_recomendadas = []
    for preferencia, actividades in preferencias_actividades.items():
        if preferencia in preferencias:
            actividades_recomendadas.extend(actividades)
    return actividades_recomendadas

# Preferencias del usuario
preferencias_usuario = ["Deportes", "Viajes"]

# Recomendar actividades basadas en las preferencias del usuario
actividades_recomendadas = recomendar_actividades(preferencias_usuario)

# Imprimir actividades recomendadas
print("Actividades recomendadas:")
for actividad in actividades_recomendadas:
    print("-", actividad)
