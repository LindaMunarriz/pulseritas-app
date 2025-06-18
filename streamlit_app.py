# streamlit_app.py
import streamlit as st
from utils.login import login, check_login

st.set_page_config(page_title="Pulseritas Co", layout="centered")

if not check_login():
    login()
    st.stop()  # Se detiene aquí si no ha iniciado sesión

# Si pasa el login, se muestra el contenido principal
st.sidebar.title("📁 Navegación")
st.sidebar.success("Selecciona una página a la izquierda ☝️")

st.write(f"¡Hola, {st.session_state.usuario.capitalize()}! 🌈✨")
st.write("Esta es nuestra app para reportar ventas, ver métricas y seguir alimentando sonrisas.")
