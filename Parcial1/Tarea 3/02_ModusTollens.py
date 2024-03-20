# Definir las premisas
premisa_1 = "Si llueve, el suelo estará mojado."
premisa_2 = "El suelo no está mojado."

# Función para aplicar el método de inferencia Modus Tollens
def modus_tollens(premisa_1, premisa_2):
    conclusion = ""
    if "no" in premisa_2:
        # Si la segunda premisa niega el resultado, inferimos la negación de la primera premisa
        conclusion = premisa_1.split(",")[0][3:]  # Extraer la parte después de "Si "
    else:
        conclusion = "No se puede aplicar el Modus Tollens."
    return conclusion

# Aplicar el método de inferencia Modus Tollens
resultado = modus_tollens(premisa_1, premisa_2)

# Imprimir el resultado
print("Resultado del Modus Tollens:", resultado)
