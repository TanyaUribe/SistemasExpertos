# Función para capturar reglas sobre el comportamiento de animales
def capturar_conocimiento():
    conocimiento = {}

    print("Por favor, introduce reglas sobre el comportamiento de animales:")
    print("Ejemplo de formato: 'Los gatos maúllan'")
    print("Escribe 'fin' para terminar la captura de conocimiento")

    while True:
        regla = input("Regla: ").strip().lower()
        if regla == "fin":
            break
        else:
            partes = regla.split(" ")
            if len(partes) >= 3 and partes[1] in ["es", "son"]:
                animal = partes[0]
                comportamiento = " ".join(partes[2:])
                if animal in conocimiento:
                    conocimiento[animal].append(comportamiento)
                else:
                    conocimiento[animal] = [comportamiento]

    return conocimiento

# Capturar conocimiento sobre el comportamiento de animales
base_de_conocimiento = capturar_conocimiento()

# Imprimir la base de conocimiento capturada
print("\nBase de conocimiento capturada:")
for animal, comportamientos in base_de_conocimiento.items():
    print(f"{animal.capitalize()} {', '.join(comportamientos)}")
