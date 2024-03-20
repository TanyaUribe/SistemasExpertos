#En este ejemplo, el motor de inferencia analiza las reglas de inferencia definidas en reglas_inferencia 
#y los hechos iniciales proporcionados en hechos_iniciales. Luego, aplica las reglas pertinentes para 
#derivar nuevas inferencias y las devuelve como resultado. Este es un ejemplo simple que ilustra el 
#proceso básico de inferencia en un sistema experto.


# Base de conocimientos: Reglas de inferencia
reglas_inferencia = {
    "Regla 1": {"Si": ["A"], "Entonces": ["B"]},
    "Regla 2": {"Si": ["B"], "Entonces": ["C"]}
}

# Función para el motor de inferencia
def motor_inferencia(hechos):
    nuevas_inferencias = set()
    for regla, condicion in reglas_inferencia.items():
        if all(cond in hechos for cond in condicion["Si"]):
            nuevas_inferencias.update(condicion["Entonces"])
    return nuevas_inferencias

# Hechos iniciales
hechos_iniciales = {"A"}

# Realizar inferencia
nuevas_inferencias = motor_inferencia(hechos_iniciales)

# Imprimir nuevas inferencias
print("Nuevas inferencias:", nuevas_inferencias)
