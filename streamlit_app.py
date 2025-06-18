# streamlit_app.py
import streamlit as st
from utils.login import login, check_login

st.set_page_config(page_title="Pulseritas Co", layout="centered")

# Mostramos login si no ha iniciado sesión
if not check_login():
    login()
    st.stop()  # IMPORTANTE: evita que el resto del código se ejecute sin login

# Si sí está logueada, ahora sí mostramos el menú
st.sidebar.title("📁 Navegación")
st.sidebar.success("Selecciona una página a la izquierda ☝️")

st.write(f"¡Hola, {st.session_state.usuario.capitalize()}! 🌈✨")
st.write("Esta es nuestra app para reportar ventas, ver métricas y seguir alimentando sonrisas.")
