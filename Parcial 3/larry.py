import sqlite3

# Conexión a la base de datos SQLite
conn = sqlite3.connect('larry.db')
cursor = conn.cursor()

# Crear tablas si no existen
cursor.execute('''
    CREATE TABLE IF NOT EXISTS hechos (
        id INTEGER PRIMARY KEY,
        hecho TEXT UNIQUE
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reglas (
        id INTEGER PRIMARY KEY,
        premisas TEXT,
        conclusion TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS intensidad_sintomas (
        id INTEGER PRIMARY KEY,
        id_sintoma INTEGER,
        intensidad TEXT,
        valor_sintoma INTEGER,
        FOREIGN KEY (id_sintoma) REFERENCES hechos (id)
    )
''')


intensidades = [
    ('poco',),
    ('medio',),
    ('alto',),
]
cursor.executemany('INSERT OR IGNORE INTO intensidad_sintomas (intensidad) VALUES (?)', intensidades)

valores = [
    (1,),
    (2,),
    (3,),
]
cursor.executemany('INSERT OR IGNORE INTO intensidad_sintomas (valor_sintoma) VALUES (?)',valores)


# Insertar datos de ejemplo
datos_hechos = [
    ('fiebre',),
    ('dolor_de_cabeza',),
    ('color_de_moco',),
    ('estornudo_constante',),
    ('cosquilleo_nasal',),
    ('ardor_garganta',),
    ('cansancio_gral',),
    ('ojos_llorosos',),
    ('goteo_nasal_congestion',),
    ('dolor_corporal',),
]

cursor.executemany('INSERT OR IGNORE INTO hechos (hecho) VALUES (?)', datos_hechos)

datos_reglas = [
    ('fiebre AND dolor_de_cabeza', 'diagnostico_posible'),
    ('tos_persistente', 'diagnostico_posible'),
]

cursor.executemany('INSERT OR IGNORE INTO reglas (premisas, conclusion) VALUES (?, ?)', datos_reglas)

# Guardar cambios y cerrar la conexión
conn.commit()
conn.close()


class SistemaExperto:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def obtener_hechos(self):
        self.cursor.execute('SELECT hecho FROM hechos')
        return [row[0] for row in self.cursor.fetchall()]

    def obtener_reglas(self):
        self.cursor.execute('SELECT premisas, conclusion FROM reglas')
        return self.cursor.fetchall()

    def evaluar_diagnostico(self, sintomas_respuestas):
        # Preparar la consulta SQL dinámica para evaluar las premisas
        consulta = "SELECT conclusion FROM reglas WHERE "
        for sintoma, respuesta in sintomas_respuestas.items():
            # Obtener el valor numérico de intensidad desde la base de datos
            self.cursor.execute(f"SELECT valor_sintoma FROM intensidad_sintomas WHERE intensidad = ?", (respuesta,))
            valor_numerico = self.cursor.fetchone()[0]

            # Construir la parte de la consulta SQL para evaluar las premisas
            consulta += f"({valor_numerico} >= (SELECT valores FROM intensidad_sintomas WHERE id_sintoma = (SELECT id FROM hechos WHERE hecho = '{sintoma}'))) AND "

       # consulta = consulta[:-5]  # Eliminar el último "AND"
        #self.cursor.execute(consulta)
        resultado = self.cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            return "No se puede determinar el diagnóstico con la información proporcionada."

    def cerrar_conexion(self):
        self.conn.close()


# Función para interactuar con el usuario
def interactuar_con_usuario():
    # Crear instancia del sistema experto y conectar a la base de datos
    sistema_experto = SistemaExperto('larry.db')

    # Obtener hechos (síntomas) desde la base de datos
    hechos = sistema_experto.obtener_hechos()

    # Pedir al usuario que ingrese la intensidad de los síntomas
    sintomas_respuestas = {}
    for hecho in hechos:
        respuesta = input(f"¿Qué intensidad tiene el síntoma '{hecho}'? (poco/medio/alto): ").strip().lower()
        while respuesta not in ['poco', 'medio', 'alto']:
            respuesta = input("Por favor, ingrese una respuesta válida (poco/medio/alto): ").strip().lower()
        sintomas_respuestas[hecho] = respuesta

    # Evaluar el diagnóstico basado en las respuestas del usuario
    diagnostico = sistema_experto.evaluar_diagnostico(sintomas_respuestas)
    print(f"\nEl diagnóstico posible es: {diagnostico}\n")

    # Cerrar la conexión con la base de datos
    sistema_experto.cerrar_conexion()

def evaluar_diagnostico(self, sintomas_respuestas):
    consulta = "SELECT conclusion FROM reglas WHERE "
    for sintoma, respuesta in sintomas_respuestas.items():
        consulta += f"('{respuesta}' >= (SELECT intensidad FROM intensidad_sintomas WHERE id_sintoma = (SELECT id FROM hechos WHERE hecho = '{sintoma}'))) AND "
    consulta = consulta[:-5]  # Eliminar el último "AND"
    self.cursor.execute(consulta)
    resultado = self.cursor.fetchone()
    if resultado:
        return resultado[0]
    else:
        return "No se puede determinar el diagnóstico con la información proporcionada."


# Ejecutar la función principal para interactuar con el usuario
if __name__ == "__main__":
    interactuar_con_usuario()

