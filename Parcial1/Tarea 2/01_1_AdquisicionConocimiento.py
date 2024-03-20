#La adquisición de conocimiento implica recopilar información sobre las 
#enfermedades de las plantas y los síntomas asociados, y luego expresar 
#esta información en forma de reglas que el sistema experto pueda utilizar 
#para realizar diagnósticos.

# Definición de reglas para el diagnóstico de enfermedades en plantas
reglas_diagnostico = {
    "Enfermedad A": {
        "Síntoma 1": "grave",
        "Síntoma 2": "moderado",
        "Síntoma 3": "leve"
    },
    "Enfermedad B": {
        "Síntoma 2": "grave",
        "Síntoma 4": "moderado",
        "Síntoma 5": "leve"
    },
    "Enfermedad C": {
        "Síntoma 1": "grave",
        "Síntoma 3": "grave",
        "Síntoma 5": "moderado"
    },
    # Agregar más reglas según sea necesario
}

# Función para realizar el diagnóstico basado en los síntomas observados
def diagnosticar_enfermedad(sintomas):
    for enfermedad, regla in reglas_diagnostico.items():
        cumple_condiciones = True
        for sintoma, severidad in regla.items():
            if sintoma in sintomas and sintomas[sintoma] != severidad:
                cumple_condiciones = False
                break
        if cumple_condiciones:
            return enfermedad
    return "No se puede determinar la enfermedad"

# Ejemplo de síntomas observados en una planta
sintomas_planta = {
    "Síntoma 1": "grave",
    "Síntoma 3": "moderado",
    "Síntoma 5": "leve"
}

# Realizar el diagnóstico
enfermedad_detectada = diagnosticar_enfermedad(sintomas_planta)
print("La planta podría tener la enfermedad:", enfermedad_detectada)
