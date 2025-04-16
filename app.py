import streamlit as st

# Datos simulados (como si vinieran de un Excel)
muestras = [
    {"nombre": "Muestra 1", "cuarzo": 92.5, "feldespato": 3.0, "fragmentos": 2.5, "accesorios": 2.0},
    {"nombre": "Muestra 2", "cuarzo": 60.0, "feldespato": 30.0, "fragmentos": 5.0, "accesorios": 5.0},
    {"nombre": "Muestra 3", "cuarzo": 55.0, "feldespato": 10.0, "fragmentos": 30.0, "accesorios": 5.0},
    {"nombre": "Muestra 4", "cuarzo": 45.0, "feldespato": 25.0, "fragmentos": 25.0, "accesorios": 5.0},
    {"nombre": "Muestra 5", "cuarzo": 85.0, "feldespato": 5.0, "fragmentos": 5.0, "accesorios": 5.0},
    {"nombre": "Muestra 6", "cuarzo": 68.0, "feldespato": 12.0, "fragmentos": 15.0, "accesorios": 5.0},
    {"nombre": "Muestra 7", "cuarzo": 40.0, "feldespato": 35.0, "fragmentos": 20.0, "accesorios": 5.0},
    {"nombre": "Muestra 8", "cuarzo": 91.0, "feldespato": 4.0, "fragmentos": 3.0, "accesorios": 2.0},
]

def clasificar_pettijohn(m):
    if m["cuarzo"] > 90:
        return "Arenita cuarzosa"
    elif m["feldespato"] > 25:
        return "Arenita arcósica"
    elif m["fragmentos"] > 25:
        return "Arenita lítica"
    else:
        return "Arenita mixta"

st.title("Clasificación de Rocas Sedimentarias - Pettijohn")

seleccion = st.selectbox("Selecciona una muestra:", [m["nombre"] for m in muestras])

muestra = next(m for m in muestras if m["nombre"] == seleccion)

st.subheader(f"Datos de {muestra['nombre']}")
st.write(f"- Cuarzo: {muestra['cuarzo']}%")
st.write(f"- Feldespato: {muestra['feldespato']}%")
st.write(f"- Fragmentos de Roca: {muestra['fragmentos']}%")
st.write(f"- Accesorios: {muestra['accesorios']}%")

clasificacion = clasificar_pettijohn(muestra)

st.success(f"📌 Clasificación según Pettijohn: **{clasificacion}**")
