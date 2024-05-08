import random
import tkinter as tk

class PersonajeDisney:
    def __init__(self, nombre, caracteristicas):
        self.nombre = nombre
        self.caracteristicas = caracteristicas

class JuegoAdivinaQuienDisney:
    def __init__(self, personajes):
        self.personajes = personajes
        self.caracteristicas_preguntadas = set()

    def hacer_pregunta(self, pregunta):
        resultados = []
        for personaje in self.personajes:
            if pregunta in personaje.caracteristicas:
                resultados.append(personaje.nombre)
        return resultados

    def obtener_pregunta(self):
        caracteristicas_disponibles = [caracteristica for caracteristica in self.personajes[0].caracteristicas if caracteristica not in self.caracteristicas_preguntadas]
        if not caracteristicas_disponibles:
            return None
        pregunta = random.choice(caracteristicas_disponibles)
        self.caracteristicas_preguntadas.add(pregunta)
        return pregunta

    def reiniciar_juego(self):
        self.caracteristicas_preguntadas.clear()

    def adivinar_personaje(self):
        return random.choice(self.personajes).nombre

def mostrar_resultado(respuesta):
    if respuesta:
        resultado_label.config(text="¡El personaje es {}!".format(respuesta))
        continuar_button.pack_forget()
        no_button.pack_forget()
        cerrar_button.pack(side=tk.RIGHT, padx=10, pady=10)
    else:
        resultado_label.config(text="No se encontró ningún personaje que coincida.")
        continuar_button.pack(side=tk.LEFT, padx=10, pady=10)
        no_button.pack(side=tk.RIGHT, padx=10, pady=10)
        cerrar_button.pack_forget()

def iniciar_juego():
    comenzar_button.pack_forget()
    siguiente_pregunta()

def responder_si():
    juego.personajes = [personaje for personaje in juego.personajes if personaje.nombre in resultados]
    if len(juego.personajes) == 1:
        mostrar_resultado(juego.personajes[0].nombre)
    else:
        siguiente_pregunta()

def responder_no():
    juego.personajes = [personaje for personaje in juego.personajes if personaje.nombre not in resultados]
    if len(juego.personajes) == 1:
        mostrar_resultado(juego.personajes[0].nombre)
    else:
        siguiente_pregunta()

def siguiente_pregunta():
    pregunta = juego.obtener_pregunta()
    if pregunta is None:
        if len(juego.personajes) == 1:
            mostrar_resultado(juego.personajes[0].nombre)
        else:
            juego.reiniciar_juego()
            siguiente_pregunta()
    else:
        pregunta_label.config(text=pregunta)
        resultados.clear()
        resultados.extend(juego.hacer_pregunta(pregunta))
        si_button.pack(side=tk.LEFT, padx=10, pady=10)
        no_button.pack(side=tk.RIGHT, padx=10, pady=10)

def continuar_juego():
    continuar_button.pack_forget()
    cerrar_button.pack_forget()
    juego.reiniciar_juego()
    siguiente_pregunta()

def cerrar_juego():
    root.destroy()

# Definir personajes y sus características de Disney
personajes = [
    PersonajeDisney("Mickey Mouse", ["Es un ratón", "Usa pantalones rojos", "Tiene guantes blancos"]),
    PersonajeDisney("Pato Donald", ["Es un pato", "Usa sombrero de marinero", "Tiene un mal genio"]),
    PersonajeDisney("Goofy", ["Es un perro", "Es torpe", "Tiene dientes grandes"]),
    PersonajeDisney("Pluto", ["Es un perro", "Es mascota de Mickey", "No habla"]),
    PersonajeDisney("Blanca Nieves", ["Es una princesa", "Vive en un bosque", "Tiene siete amigos enanos"]),
    PersonajeDisney("Cenicienta", ["Es una princesa","Tiene cabello rubio", "Pierde su zapatilla"]),
    PersonajeDisney("Ariel", ["Es una princesa", "Vive en el mar", "Es una sirena"]),
    PersonajeDisney("Rapunzel",["Es una princesa","Tiene cabello rubio","Tiene un camaleon de mascota"])
    # Agrega más personajes y características de Disney aquí
]

# Crear el juego
juego = JuegoAdivinaQuienDisney(personajes)
resultados = []

# Configurar ventana
root = tk.Tk()
root.title("Adivina Quién - Personajes de Disney")

# Etiqueta para mostrar la pregunta
pregunta_label = tk.Label(root, text="Piensa en un personaje clásico de Disney y responde a las siguientes preguntas con 'si' o 'no':\nMickeyMouse\nPatoDonald\nGoofy\nPluto\nBlancaNieves\nCenicienta\nAriel\nRapunzel")
pregunta_label.pack(padx=10, pady=10)

# Botones para responder si o no
si_button = tk.Button(root, text="Sí", command=responder_si)
no_button = tk.Button(root, text="No", command=responder_no)

# Botón para comenzar
comenzar_button = tk.Button(root, text="Comencemos!", command=iniciar_juego)
comenzar_button.pack(padx=10, pady=10)

# Botones para continuar o cerrar el juego
continuar_button = tk.Button(root, text="Continuar", command=continuar_juego)
cerrar_button = tk.Button(root, text="Cerrar", command=cerrar_juego)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(root, text="")
resultado_label.pack(padx=10, pady=10)

# Iniciar la ventana
root.mainloop()
