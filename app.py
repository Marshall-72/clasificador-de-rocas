import streamlit as st
import matplotlib.pyplot as plt

# Datos simulados de 8 muestras sedimentarias
muestras = [
     {
        "nombre": "Arenisca Cuarzosa",
        "tipo_particula": {"grava": 5, "arena": 90, "lodo": 5},
        "componentes": {"armazon": 80, "matriz": 10, "cemento": 5, "porosidad": 5},
        "forma": {"esfericidad": 0.7, "redondez": 0.8, "seleccion": "buena", "madurez": "alta"},
        "color": "blanco amarillento", "color_alteracion": "ocre claro",
        "minerales": {"cuarzo": 75, "feldespatos": 5, "fragmentos_roca": 10, "accesorios": 10}
    },
    {
        "nombre": "Arcosa",
        "tipo_particula": {"grava": 5, "arena": 85, "lodo": 10},
        "componentes": {"armazon": 65, "matriz": 20, "cemento": 10, "porosidad": 5},
        "forma": {"esfericidad": 0.6, "redondez": 0.7, "seleccion": "moderada", "madurez": "media"},
        "color": "rosado", "color_alteracion": "gris rojizo",
        "minerales": {"cuarzo": 50, "feldespatos": 30, "fragmentos_roca": 15, "accesorios": 5}
    },
    {
        "nombre": "Conglomerado Polimíctico",
        "tipo_particula": {"grava": 80, "arena": 15, "lodo": 5},
        "componentes": {"armazon": 70, "matriz": 20, "cemento": 5, "porosidad": 5},
        "forma": {"esfericidad": 0.8, "redondez": 0.9, "seleccion": "pobre", "madurez": "baja"},
        "color": "gris claro", "color_alteracion": "marrón",
        "minerales": {"cuarzo": 40, "feldespatos": 10, "fragmentos_roca": 45, "accesorios": 5}
    },
    {
        "nombre": "Brecha",
        "tipo_particula": {"grava": 75, "arena": 20, "lodo": 5},
        "componentes": {"armazon": 65, "matriz": 25, "cemento": 5, "porosidad": 5},
        "forma": {"esfericidad": 0.6, "redondez": 0.4, "seleccion": "pobre", "madurez": "muy baja"},
        "color": "gris oscuro", "color_alteracion": "rojizo",
        "minerales": {"cuarzo": 35, "feldespatos": 15, "fragmentos_roca": 45, "accesorios": 5}
    },
    {
        "nombre": "Lutita",
        "tipo_particula": {"grava": 0, "arena": 10, "lodo": 90},
        "componentes": {"armazon": 20, "matriz": 70, "cemento": 5, "porosidad": 5},
        "forma": {"esfericidad": 0.3, "redondez": 0.2, "seleccion": "muy buena", "madurez": "alta"},
        "color": "negro", "color_alteracion": "gris verdoso",
        "minerales": {"cuarzo": 30, "feldespatos": 5, "fragmentos_roca": 10, "accesorios": 55}
    },
    {
        "nombre": "Arenita",
        "tipo_particula": {"grava": 0, "arena": 85, "lodo": 15},
        "componentes": {"armazon": 75, "matriz": 15, "cemento": 5, "porosidad": 5},
        "forma": {"esfericidad": 0.7, "redondez": 0.8, "seleccion": "buena", "madurez": "media"},
        "color": "beige", "color_alteracion": "amarillo pálido",
        "minerales": {"cuarzo": 60, "feldespatos": 20, "fragmentos_roca": 15, "accesorios": 5}
    },
    {
        "nombre": "Arenisca Piroclástica",
        "tipo_particula": {"grava": 10, "arena": 80, "lodo": 10},
        "componentes": {"armazon": 60, "matriz": 25, "cemento": 10, "porosidad": 5},
        "forma": {"esfericidad": 0.6, "redondez": 0.7, "seleccion": "moderada", "madurez": "baja"},
        "color": "gris claro", "color_alteracion": "rosado claro",
        "minerales": {"cuarzo": 40, "feldespatos": 20, "fragmentos_roca": 25, "accesorios": 15}
    },
    {
        "nombre": "Arenisca de grano grueso",
        "tipo_particula": {"grava": 10, "arena": 85, "lodo": 5},
        "componentes": {"armazon": 70, "matriz": 15, "cemento": 10, "porosidad": 5},
        "forma": {"esfericidad": 0.75, "redondez": 0.65, "seleccion": "moderada", "madurez": "media"},
        "color": "amarillo claro", "color_alteracion": "ocre amarillento",
        "minerales": {"cuarzo": 65, "feldespatos": 15, "fragmentos_roca": 15, "accesorios": 5}
    }
]

# Interfaz Streamlit
st.title("Comparación de Muestras Sedimentarias")

muestras_nombres = [m["nombre"] for m in muestras]
seleccionadas = st.multiselect("Selecciona muestras para comparar:", muestras_nombres, default=muestras_nombres[:2])

# Filtro de datos
muestras_filtradas = [m for m in muestras if m["nombre"] in seleccionadas]

# Gráfico de distribución de tamaño de partículas
if muestras_filtradas:
    # Gráfico de distribución de tamaño de partículas
    fig, ax = plt.subplots(figsize=(10, 6))
    ancho = 0.2
    x = range(len(muestras_filtradas))

    for i, comp in enumerate(["grava", "arena", "lodo"]):
        valores = [m["tipo_particula"][comp] for m in muestras_filtradas]
        ax.bar([v + ancho*i for v in x], valores, width=ancho, label=comp)

    ax.set_xticks([v + ancho for v in x])
    ax.set_xticklabels([m["nombre"] for m in muestras_filtradas], rotation=45)
    ax.set_ylabel("Porcentaje (%)")
    ax.set_title("Distribución de Tamaño de Partículas")
    ax.legend()
    ax.text(0.5, -0.2, 'Fuente: Cutipa, C. Quenaya, F. Jaramillo, A. Amaro, M.', transform=ax.transAxes, ha='center', fontsize=8)
    st.pyplot(fig)

    # Gráfico de forma y madurez
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    esfericidad = [m["forma"]["esfericidad"] for m in muestras_filtradas]
    redondez = [m["forma"]["redondez"] for m in muestras_filtradas]
    nombres = [m["nombre"] for m in muestras_filtradas]

    ax2.scatter(esfericidad, redondez, c='green', s=100)
    for i, nombre in enumerate(nombres):
        ax2.text(esfericidad[i] + 0.01, redondez[i], nombre, fontsize=8)
    ax2.set_xlabel("Esfericidad")
    ax2.set_ylabel("Redondez")
    ax2.set_title("Esfericidad vs Redondez")
    ax2.text(0.5, -0.2, 'Fuente: Cutipa, C. Quenaya, F. Jaramillo, A. Amaro, M.', transform=ax2.transAxes, ha='center', fontsize=8)
    st.pyplot(fig2)

    # Gráfico de composición mineral
    fig3, ax3 = plt.subplots(figsize=(10, 6))
    ancho = 0.2
    x = range(len(muestras_filtradas))
    for i, comp in enumerate(["cuarzo", "feldespatos", "fragmentos_roca", "accesorios"]):
        valores = [m["minerales"][comp] for m in muestras_filtradas]
        ax3.bar([v + ancho*i for v in x], valores, width=ancho, label=comp)

    ax3.set_xticks([v + ancho*1.5 for v in x])
    ax3.set_xticklabels([m["nombre"] for m in muestras_filtradas], rotation=45)
    ax3.set_ylabel("Porcentaje (%)")
    ax3.set_title("Composición Mineral de las Muestras")
    ax3.legend()
    ax3.text(0.5, -0.2, 'Fuente: Cutipa, C. Quenaya, F. Jaramillo, A. Amaro, M.', transform=ax3.transAxes, ha='center', fontsize=8)
    st.pyplot(fig3)

    # Gráfico de composición interna: armazón, matriz, cemento y porosidad
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    x = range(len(muestras_filtradas))

    armazon = [m["componentes"]["armazon"] for m in muestras_filtradas]
    matriz = [m["componentes"]["matriz"] for m in muestras_filtradas]
    cemento = [m["componentes"]["cemento"] for m in muestras_filtradas]
    porosidad = [m["componentes"]["porosidad"] for m in muestras_filtradas]

    ax4.bar(x, armazon, label="Armazón")
    ax4.bar(x, matriz, bottom=armazon, label="Matriz")
    bottom_cem = [a + b for a, b in zip(armazon, matriz)]
    ax4.bar(x, cemento, bottom=bottom_cem, label="Cemento")
    bottom_por = [a + b + c for a, b, c in zip(armazon, matriz, cemento)]
    ax4.bar(x, porosidad, bottom=bottom_por, label="Porosidad")

    ax4.set_xticks(x)
    ax4.set_xticklabels([m["nombre"] for m in muestras_filtradas], rotation=45)
    ax4.set_ylabel("Porcentaje (%)")
    ax4.set_title("Composición Interna de las Muestras")
    ax4.legend()
    ax4.text(0.5, -0.2, 'Fuente: Cutipa, C. Quenaya, F. Jaramillo, A. Amaro, M.', transform=ax4.transAxes, ha='center', fontsize=8)
    st.pyplot(fig4)
    
    # Tabla resumen
    st.write("### Resumen de Composición Mineral")
    for m in muestras_filtradas:
        st.write(f"**{m['nombre']}**")
        st.write(m["minerales"])



# Lista de preguntas y respuestas predefinidas, con varias respuestas posibles
preguntas_respuestas = {
    "Defina con sus palabras qué relación existe entre el tipo de contacto de las partículas y la matriz.": 
        {"respuestas": [
            "El contacto entre las partículas de una roca sedimentaria puede ser puntual, lineal o superficial, y la matriz es el material que llena los espacios entre las partículas. A mayor contacto, menor es la cantidad de matriz, lo que influye en la porosidad y otras características.",
            "El tipo de contacto entre las partículas influye directamente en la cantidad de matriz. Cuando las partículas están más unidas, la matriz tiende a ser menor, lo que puede mejorar las propiedades de la roca.",
            "La relación entre el contacto de las partículas y la matriz es importante porque afecta la porosidad. A medida que las partículas están más cerca unas de otras, el espacio entre ellas es ocupado por la matriz, lo que puede disminuir la porosidad."
        ],
        "palabras_clave": ["contacto", "partículas", "matriz"]},
    
    "Si una roca sedimentaria siliciclástica es madura texturalmente, ¿qué se puede decir del contenido de matriz, el sortamiento y la redondez?": 
        {"respuestas": [
            "Una roca madura texturalmente tiene poco contenido de matriz, ya que las partículas están bien seleccionadas y son redondeadas. El sortamiento es muy bueno, lo que significa que las partículas son de tamaño uniforme.",
            "Las rocas maduras texturalmente presentan una baja cantidad de matriz y una excelente redondez de las partículas. El sortamiento es muy bueno, lo que refleja un transporte prolongado.",
            "Cuando una roca es madura texturalmente, las partículas son redondeadas, bien seleccionadas y el contenido de matriz es bajo. El sortamiento es bueno, lo que indica una larga historia de transporte."
        ],
        "palabras_clave": ["madura", "texturalmente", "matriz", "sortamiento", "redondez"]},
    
    "Una roca sedimentaria siliciclástica al ser observada en muestra de mano presenta un mal calibrado, ¿qué se puede interpretar de esto?": 
        {"respuestas": [
            "El mal calibrado indica que las partículas no están bien ordenadas en tamaños, lo que puede sugerir que la roca es inmadura texturalmente o que ha sido depositada en condiciones dinámicas no estables.",
            "Un mal calibrado de la muestra sugiere que la roca tiene una distribución de tamaños de partículas muy heterogénea, lo que indica un entorno de deposición más caótico o rápido.",
            "Cuando las partículas no están bien calibradas, puede indicar que la roca tiene un origen en un ambiente de deposición más inestable, lo que podría reflejar una roca inmadura."
        ],
        "palabras_clave": ["muestra de mano", "calibrado", "partículas", "inmadura"]},
    
    "¿Cuál es la diferencia que existe entre matriz y cemento? ¿Cómo se pueden distinguir macroscópicamente?": 
        {"respuestas": [
            "La matriz es el material fino que ocupa los espacios entre las partículas, mientras que el cemento es una sustancia mineral que une las partículas. Macroscópicamente, el cemento tiene una textura más sólida y cristalina, mientras que la matriz suele ser más fina y menos compacta.",
            "La matriz ocupa los vacíos entre los clastos, mientras que el cemento es lo que liga los clastos entre sí. Macroscópicamente, el cemento es más duro y cristalino en comparación con la matriz.",
            "La matriz es un material que llena los vacíos entre los clastos, mientras que el cemento solidifica y une los clastos. El cemento es más evidente bajo el microscopio por su dureza y estructura, mientras que la matriz es más fina."
        ],
        "palabras_clave": ["matriz", "cemento", "macroscópicamente", "partículas"]},
    
    "¿Por qué es importante definir el porcentaje de matriz en la roca en términos de clasificación?": 
        {"respuestas": [
            "El porcentaje de matriz es crucial porque ayuda a clasificar las rocas en términos de madurez y porosidad. Una mayor cantidad de matriz generalmente indica una roca inmadura y de baja porosidad.",
            "Definir el porcentaje de matriz permite clasificar mejor la roca, ya que una roca con alta matriz suele ser inmadura, mientras que una con poca matriz indica madurez.",
            "El porcentaje de matriz es importante en la clasificación porque permite entender la historia de la roca. Una roca con bajo porcentaje de matriz tiende a ser más madura y tener mayor porosidad."
        ],
        "palabras_clave": ["porcentaje", "matriz", "clasificación", "madurez", "porosidad"]},
    
    "Cuando una roca es un conglomerado, ¿qué clasificaciones hay?": 
        {"respuestas": [
            "Un conglomerado se clasifica en función de la cantidad de matriz y el tamaño de los clastos. Dependiendo del porcentaje de matriz, se puede clasificar como un conglomerado rudítico o como un brecho.",
            "Los conglomerados se pueden clasificar según el tamaño de los clastos y el contenido de matriz. En función de estos factores, pueden ser conglomerados rudíticos o brechos.",
            "Dependiendo del contenido de matriz y el tamaño de los clastos, los conglomerados se pueden clasificar en conglomerados de grano fino o grueso, e incluso en brechos si los clastos son muy grandes."
        ],
        "palabras_clave": ["conglomerado", "clasificación", "matriz", "clastos"]},
    
    "¿En qué consiste la madurez composicional de una roca?": 
        {"respuestas": [
            "La madurez composicional hace referencia al grado de alteración de los minerales originales en una roca. En rocas maduras, los minerales más susceptibles a la alteración han sido transformados o removidos, dejando una composición más estable.",
            "La madurez composicional describe el grado en que los minerales reactivos han sido eliminados de la roca, dejando una composición más estable y resistente.",
            "Una roca madura composicionalmente tiene pocos minerales alterados y una mayor estabilidad en su composición. Los minerales más reactivos han sido transformados o eliminados."
        ],
        "palabras_clave": ["madurez", "composicional", "alteración", "minerales"]},
    
    "¿Qué diferencia existe entre porosidad y permeabilidad?": 
        {"respuestas": [
            "La porosidad es la cantidad de espacio vacío dentro de la roca, mientras que la permeabilidad es la capacidad de la roca para permitir el paso de fluidos. Una roca puede tener alta porosidad pero baja permeabilidad si los poros no están conectados.",
            "La porosidad se refiere al volumen de espacio vacío dentro de la roca, mientras que la permeabilidad es la facilidad con la que los fluidos pueden fluir a través de esos espacios.",
            "La porosidad mide los vacíos dentro de la roca, mientras que la permeabilidad describe cómo los fluidos pueden moverse a través de esos vacíos. Una roca puede tener alta porosidad pero baja permeabilidad si los poros no están interconectados."
        ],
        "palabras_clave": ["porosidad", "permeabilidad", "espacio vacío", "fluidos"]},
    
    "¿Una roca puede presentar tanto porosidades de tipo primarias y secundarias? Explique brevemente.": 
        {"respuestas": [
            "Sí, una roca puede presentar porosidad primaria (formada durante la sedimentación) y porosidad secundaria (formada por procesos posteriores como fracturamiento o meteorización). Ambas porosidades pueden coexistir y afectar las propiedades de la roca.",
            "Es posible que una roca tenga porosidad primaria, que se forma durante la deposición, y porosidad secundaria, que se desarrolla por fracturamientos o alteraciones posteriores. Ambas porosidades influyen en las características de la roca.",
            "Las rocas pueden presentar tanto porosidad primaria, que es la original de la sedimentación, como porosidad secundaria, que surge debido a procesos posteriores como la fracturación. Ambas son importantes para la permeabilidad y porosidad de la roca."
        ],
        "palabras_clave": ["porosidad", "primaria", "secundaria", "fracturamiento", "meteorización"]}
}

# Función para obtener una respuesta aleatoria
def obtener_respuesta(pregunta_usuario):
    respuesta = "Lo siento, no pude encontrar una respuesta adecuada."
    
    # Convertir la pregunta del usuario en una lista de palabras clave
    palabras_usuario = pregunta_usuario.lower().split()
    
    # Buscar las palabras clave en las preguntas predefinidas
    for pregunta, info in preguntas_respuestas.items():
        palabras_clave = info["palabras_clave"]
        
        # Contar cuántas palabras clave coinciden
        coincidencias = sum(1 for palabra in palabras_usuario if palabra in palabras_clave)
        
        # Si encontramos coincidencias, devolver una respuesta aleatoria
        if coincidencias >= 2:  # Este umbral se puede ajustar
            # Seleccionar una respuesta aleatoria de la lista
            respuesta = info["respuestas"][hash(pregunta_usuario) % len(info["respuestas"])]
            break
    
    return respuesta

# Menú desplegable de preguntas
st.title("Preguntas Interpretativas sobre Rocas Sedimentarias")

# Opción 1: Menú desplegable
st.subheader("Selecciona una pregunta")
pregunta_seleccionada = st.selectbox("Elige una pregunta:", list(preguntas_respuestas.keys()))

if pregunta_seleccionada:
    st.write("**Respuesta:**")
    st.write(preguntas_respuestas[pregunta_seleccionada]["respuestas"][hash(pregunta_seleccionada) % len(preguntas_respuestas[pregunta_seleccionada]["respuestas"])])

# Opción 2: Búsqueda de pregunta por similitud
st.subheader("Escribe tu pregunta")

pregunta_usuario = st.text_input("Escribe tu pregunta aquí:")

if pregunta_usuario:
    respuesta_similar = obtener_respuesta(pregunta_usuario)
    st.write("**Respuesta similar:**")
    st.write(respuesta_similar)





