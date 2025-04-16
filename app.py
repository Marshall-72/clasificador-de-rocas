import streamlit as st
import matplotlib.pyplot as plt

# Datos simulados de 8 muestras sedimentarias
muestras = [
    {
        "nombre": "Conglomerado",
        "tipo_particula": {"grava": 80, "arena": 15, "lodo": 5},
        "componentes": {"armazon": 70, "matriz": 20, "porosidad": 10},
        "forma": {"esfericidad": 0.8, "redondez": 0.9, "seleccion": "pobre", "madurez": "baja"},
        "color": "gris claro", "color_alteracion": "marrón",
        "minerales": {"cuarzo": 40, "feldespatos": 10, "fragmentos_roca": 45, "accesorios": 5}
    },
    {
        "nombre": "Brecha",
        "tipo_particula": {"grava": 75, "arena": 20, "lodo": 5},
        "componentes": {"armazon": 65, "matriz": 25, "porosidad": 10},
        "forma": {"esfericidad": 0.6, "redondez": 0.4, "seleccion": "pobre", "madurez": "muy baja"},
        "color": "gris oscuro", "color_alteracion": "rojizo",
        "minerales": {"cuarzo": 35, "feldespatos": 15, "fragmentos_roca": 45, "accesorios": 5}
    },
    {
        "nombre": "Lutita",
        "tipo_particula": {"grava": 0, "arena": 10, "lodo": 90},
        "componentes": {"armazon": 20, "matriz": 70, "porosidad": 10},
        "forma": {"esfericidad": 0.3, "redondez": 0.2, "seleccion": "muy buena", "madurez": "alta"},
        "color": "negro", "color_alteracion": "gris verdoso",
        "minerales": {"cuarzo": 30, "feldespatos": 5, "fragmentos_roca": 10, "accesorios": 55}
    },
    {
        "nombre": "Arenisca Fina",
        "tipo_particula": {"grava": 0, "arena": 85, "lodo": 15},
        "componentes": {"armazon": 75, "matriz": 15, "porosidad": 10},
        "forma": {"esfericidad": 0.7, "redondez": 0.8, "seleccion": "buena", "madurez": "media"},
        "color": "beige", "color_alteracion": "amarillo pálido",
        "minerales": {"cuarzo": 60, "feldespatos": 20, "fragmentos_roca": 15, "accesorios": 5}
    },
    {
        "nombre": "Arenisca Gruesa",
        "tipo_particula": {"grava": 10, "arena": 80, "lodo": 10},
        "componentes": {"armazon": 80, "matriz": 10, "porosidad": 10},
        "forma": {"esfericidad": 0.6, "redondez": 0.7, "seleccion": "moderada", "madurez": "media"},
        "color": "amarillo", "color_alteracion": "ocre",
        "minerales": {"cuarzo": 55, "feldespatos": 25, "fragmentos_roca": 15, "accesorios": 5}
    },
    {
        "nombre": "Arcillolita",
        "tipo_particula": {"grava": 0, "arena": 5, "lodo": 95},
        "componentes": {"armazon": 10, "matriz": 80, "porosidad": 10},
        "forma": {"esfericidad": 0.2, "redondez": 0.1, "seleccion": "muy buena", "madurez": "alta"},
        "color": "gris azul", "color_alteracion": "verde grisáceo",
        "minerales": {"cuarzo": 25, "feldespatos": 10, "fragmentos_roca": 15, "accesorios": 50}
    },
    {
        "nombre": "Grauvaca",
        "tipo_particula": {"grava": 5, "arena": 70, "lodo": 25},
        "componentes": {"armazon": 50, "matriz": 40, "porosidad": 10},
        "forma": {"esfericidad": 0.5, "redondez": 0.5, "seleccion": "moderada", "madurez": "baja"},
        "color": "gris verdoso", "color_alteracion": "marrón grisáceo",
        "minerales": {"cuarzo": 45, "feldespatos": 30, "fragmentos_roca": 20, "accesorios": 5}
    },
    {
        "nombre": "Marga",
        "tipo_particula": {"grava": 0, "arena": 25, "lodo": 75},
        "componentes": {"armazon": 30, "matriz": 60, "porosidad": 10},
        "forma": {"esfericidad": 0.4, "redondez": 0.3, "seleccion": "pobre", "madurez": "media"},
        "color": "crema", "color_alteracion": "gris amarillento",
        "minerales": {"cuarzo": 35, "feldespatos": 15, "fragmentos_roca": 20, "accesorios": 30}
    },
]

# Interfaz Streamlit
st.title("Comparación de Muestras Sedimentarias")

muestras_nombres = [m["nombre"] for m in muestras]
seleccionadas = st.multiselect("Selecciona muestras para comparar:", muestras_nombres, default=muestras_nombres[:2])

# Filtro de datos
muestras_filtradas = [m for m in muestras if m["nombre"] in seleccionadas]

# Gráfico de distribución de tamaño de partículas
if muestras_filtradas:
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
    ax.text(0.5, -0.2, 'Fuente: Elaboración propia', transform=ax.transAxes, ha='center', fontsize=8)
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
    ax2.text(0.5, -0.2, 'Fuente: Elaboración propia', transform=ax2.transAxes, ha='center', fontsize=8)
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
    ax3.text(0.5, -0.2, 'Fuente: Elaboración propia', transform=ax3.transAxes, ha='center', fontsize=8)
    st.pyplot(fig3)

# Tabla resumen
    st.write("### Resumen de Composición Mineral")
    for m in muestras_filtradas:
        st.write(f"**{m['nombre']}**")
        st.write(m["minerales"])


