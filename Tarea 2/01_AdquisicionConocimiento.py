# Importar la librería para sistemas expertos
from experta import *


# Definir la clase de hechos
class Síntoma(Fact):
    """Clase que define los síntomas del paciente."""
    pass


# Definir las reglas del sistema experto
class Diagnóstico(Esqueleto):
    """Clase que define las reglas del sistema experto."""

    # Regla 1: Si el paciente tiene fiebre, entonces podría tener gripe
    @Regla(Síntoma(fiebre=True))
    def gripe(self):
        self.declare(Síntoma(enfermedad="gripe"))

    # Regla 2: Si el paciente tiene tos y dolor de garganta, entonces podría tener resfriado
    @Regla(AND(Síntoma(tos=True), Síntoma(dolor_de_garganta=True)))
    def resfriado(self):
        self.declare(Síntoma(enfermedad="resfriado"))

    # Regla 3: Si no se cumple ninguna de las reglas anteriores, entonces no se puede hacer un diagnóstico
    @Regla(NEG(OR(Síntoma(fiebre=True), AND(Síntoma(tos=True), Síntoma(dolor_de_garganta=True)))))
    def desconocido(self):
        self.declare(Síntoma(enfermedad="desconocida"))


# Función principal
def main():
    # Crear un nuevo motor de inferencia
    motor = Diagnóstico()

    # Crear un nuevo hecho con los síntomas del paciente
    paciente = Síntoma(fiebre=True, tos=True, dolor_de_garganta=True)

    # Ejecutar el motor de inferencia con los síntomas del paciente
    motor.reset()
    motor.declare(paciente)
    motor.run()

    # Obtener el diagnóstico resultante
    enfermedad = motor.facts[-1].get("enfermedad")
    print("El diagnóstico es:", enfermedad)


# Ejecutar la función principal
if __name__ == "__main__":
    main()
