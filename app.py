
import streamlit as st
import matplotlib.pyplot as plt

# Función para calcular los porcentajes de los componentes
def calcular_componentes():
    st.title("Clasificador de Componentes Sedimentarios")
    st.write("Ingresa las cantidades relativas (pueden ser conteos, proporciones, etc.)")
    st.write("El programa calculará los porcentajes automáticamente.")

    # Terrígenos / Siliciclásticos
    cuarzo = st.number_input("Cuarzo: ", 0.0)
    feldespato = st.number_input("Feldespato: ", 0.0)
    fragmentos_roca = st.number_input("Fragmentos de roca: ", 0.0)

    # Aloquímicos
    conchas = st.number_input("Conchas: ", 0.0)
    oolitos = st.number_input("Oolitos: ", 0.0)
    pellets = st.number_input("Pellets: ", 0.0)
    retrabajados = st.number_input("Fragmentos retrabajados: ", 0.0)

    # Ortoquímicos
    calcita = st.number_input("Calcita microcristalina: ", 0.0)
    lodo = st.number_input("Lodo dolomítico: ", 0.0)
    evaporitas = st.number_input("Minerales evaporíticos: ", 0.0)
    chert = st.number_input("Chert / relleno de poros (calcita, cuarzo, óxidos Fe-Mn): ", 0.0)

    # Suma total
    total = (cuarzo + feldespato + fragmentos_roca +
             conchas + oolitos + pellets + retrabajados +
             calcita + lodo + evaporitas + chert)

    if total == 0:
        st.write("⚠️ No se ingresaron datos válidos.")
        return

    # Cálculo de porcentajes
    terrigenos = (cuarzo + feldespato + fragmentos_roca) / total * 100
    aloquimicos = (conchas + oolitos + pellets + retrabajados) / total * 100
    ortoquimicos = (calcita + lodo + evaporitas + chert) / total * 100

    # Resultados
    st.write(f"Terrígenos / Siliciclásticos: {terrigenos:.2f}%")
    st.write(f"Aloquímicos: {aloquimicos:.2f}%")
    st.write(f"Ortoquímicos: {ortoquimicos:.2f}%")

    # Clasificación simple
    if terrigenos > aloquimicos and terrigenos > ortoquimicos:
        st.write("→ Roca terrígena dominante (arenisca, lutita, conglomerado, etc.)")
    elif aloquimicos > terrigenos and aloquimicos > ortoquimicos:
        st.write("→ Roca carbonatada aloquímica (grainstone, packstone, etc.)")
    elif ortoquimicos > terrigenos and ortoquimicos > aloquimicos:
        st.write("→ Roca ortoquímica (micrita, dolomita, chert, evaporitas)")
    else:
        st.write("→ Composición mixta, no hay un grupo claramente dominante.")

if __name__ == "__main__":
    calcular_componentes()
