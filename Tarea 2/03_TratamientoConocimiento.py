# Base de conocimientos inicial: Reglas de diagnóstico
base_conocimientos = {
    "Enfermedad A": {"Síntoma 1": True, "Síntoma 2": False, "Síntoma 3": True},
    "Enfermedad B": {"Síntoma 1": False, "Síntoma 2": True, "Síntoma 4": True},
    "Enfermedad C": {"Síntoma 1": True, "Síntoma 3": False, "Síntoma 5": True}
}

# Función para diagnosticar enfermedades basada en síntomas observados
def diagnosticar_enfermedad(sintomas):
    enfermedades_posibles = []
    for enfermedad, regla in base_conocimientos.items():
        cumple_condiciones = all(regla[sintoma] == sintomas.get(sintoma, False) for sintoma in regla)
        if cumple_condiciones:
            enfermedades_posibles.append(enfermedad)
    return enfermedades_posibles

# Síntomas observados
sintomas_planta = {"Síntoma 1": True, "Síntoma 3": False, "Síntoma 5": True}

# Realizar el diagnóstico inicial
enfermedades_detectadas = diagnosticar_enfermedad(sintomas_planta)
print("Enfermedades detectadas inicialmente:", enfermedades_detectadas)

# Agregar una nueva regla a la base de conocimientos
nueva_regla = {"Enfermedad D": {"Síntoma 2": True, "Síntoma 4": False, "Síntoma 5": True}}
base_conocimientos.update(nueva_regla)

# Realizar un diagnóstico después de agregar la nueva regla
enfermedades_detectadas_despues = diagnosticar_enfermedad(sintomas_planta)
print("Enfermedades detectadas después de agregar la nueva regla:", enfermedades_detectadas_despues)
