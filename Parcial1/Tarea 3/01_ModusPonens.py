# Base de conocimientos: Reglas de inferencia (Modus Ponens)
reglas_inferencia = {
    "Si llueve, entonces el suelo estará mojado": True,
    "Está lloviendo": True
}

# Función para el método de inferencia Modus Ponens
def modus_ponens(reglas):
    if reglas["Está lloviendo"]:
        conclusion = "El suelo estará mojado"
        return conclusion if reglas.get(conclusion) else "No se puede inferir la conclusión"
    else:
        return "No se puede aplicar Modus Ponens"

# Realizar inferencia con Modus Ponens
resultado = modus_ponens(reglas_inferencia)

# Imprimir resultado de la inferencia
print("Resultado de la inferencia:", resultado)
