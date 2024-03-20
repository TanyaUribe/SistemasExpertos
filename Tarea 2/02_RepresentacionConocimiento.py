# Base de conocimientos: Reglas de diagnóstico
reglas_diagnostico = {
    "Enfermedad A": {"Síntoma 1": True, "Síntoma 2": False, "Síntoma 3": True},
    "Enfermedad B": {"Síntoma 1": False, "Síntoma 2": True, "Síntoma 4": True},
    "Enfermedad C": {"Síntoma 1": True, "Síntoma 3": False, "Síntoma 5": True}
}

# Función para diagnosticar enfermedades basada en síntomas observados
def diagnosticar_enfermedad(sintomas):
    enfermedades_posibles = []
    for enfermedad, regla in reglas_diagnostico.items():
        cumple_condiciones = all(regla[sintoma] == sintomas.get(sintoma, False) for sintoma in regla)
        if cumple_condiciones:
            enfermedades_posibles.append(enfermedad)
    return enfermedades_posibles

# Síntomas observados
sintomas_planta = {"Síntoma 1": True, "Síntoma 3": False, "Síntoma 5": True}

# Realizar el diagnóstico
enfermedades_detectadas = diagnosticar_enfermedad(sintomas_planta)
if enfermedades_detectadas:
    print("La planta podría tener las siguientes enfermedades:", ", ".join(enfermedades_detectadas))
else:
    print("No se pudo determinar la enfermedad")
