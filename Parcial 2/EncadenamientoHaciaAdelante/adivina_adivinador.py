import random

class Personaje:
    def __init__(self, nombre, cabello, ojos, genero, sombrero, lentes):
        self.nombre = nombre
        self.cabello = cabello
        self.ojos = ojos
        self.genero = genero
        self.sombrero = sombrero
        self.lentes = lentes

    def mostrar_caracteristicas(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cabello: {self.cabello}")
        print(f"Ojos: {self.ojos}")
        print(f"Género: {self.genero}")
        print(f"Sombrero: {'Sí' if self.sombrero else 'No'}")
        print(f"Lentes: {'Sí' if self.lentes else 'No'}")
        print()

class AdivinaQuien:
    def __init__(self, personajes):
        self.personajes = personajes

    def jugar(self):
        personaje_a_adivinar = random.choice(self.personajes)
        print("¡Bienvenido a Adivina Quién!")
        print("Tu objetivo es adivinar el personaje secreto.")
        print("Aquí están los personajes:")
        for i, personaje in enumerate(self.personajes, start=1):
            print(f"{i}. {personaje.nombre}")
        print()
        while True:
            caracteristica = input("¿Qué característica deseas preguntar? (cabello, ojos, género, sombrero, lentes): ")
            if caracteristica == "salir":
                print("¡Hasta luego!")
                break
            valor = input(f"¿Cuál es el valor de la característica '{caracteristica}' que quieres preguntar? ")
            personajes_con_caracteristica = [personaje for personaje in self.personajes if getattr(personaje, caracteristica) == valor]
            print("Personajes con esa característica:")
            for personaje in personajes_con_caracteristica:
                personaje.mostrar_caracteristicas()
            if len(personajes_con_caracteristica) == 1:
                if personajes_con_caracteristica[0] == personaje_a_adivinar:
                    print("¡Has adivinado el personaje secreto! ¡Felicidades!")
                else:
                    print("Lo siento, ese no es el personaje secreto. ¡Inténtalo de nuevo!")
                break

# Crear algunos personajes
personajes = [
    Personaje("Ana", "Rubio", "Verdes", "Mujer", False, False),
    Personaje("Pedro", "Negro", "Marrones", "Hombre", True, True),
    Personaje("María", "Castaño", "Azules", "Mujer", False, True),
    Personaje("Juan", "Pelirrojo", "Verdes", "Hombre", True, False),
]

# Iniciar el juego
juego = AdivinaQuien(personajes)
juego.jugar()
