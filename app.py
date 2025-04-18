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
    ax4.text(0.5, -0.2, 'Fuente: Elaboración propia', transform=ax4.transAxes, ha='center', fontsize=8)
    st.pyplot(fig4)
# Tabla resumen
    st.write("### Resumen de Composición Mineral")
    for m in muestras_filtradas:
        st.write(f"**{m['nombre']}**")
        st.write(m["minerales"])

import streamlit as st
import requests

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
headers = {"Authorization": f"Bearer {st.secrets['huggingface']['api_key']}"}

# Función para enviar la consulta al modelo
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Título de la app
st.title("💬 Pregúntale a la IA (vía Hugging Face)")

# Entrada del usuario
user_input = st.text_input("Escribe tu pregunta:")

if st.button("Enviar"):
    if user_input.strip() == "":
        st.warning("Por favor escribe una pregunta.")
    else:
        with st.spinner("Pensando..."):
            output = query({"inputs": user_input})
            if "error" in output:
                st.error(f"Error del modelo: {output['error']}")
            else:
                st.success("Respuesta de la IA:")
                st.write(output[0]["generated_text"])



