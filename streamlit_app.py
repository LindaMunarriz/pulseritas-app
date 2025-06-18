import streamlit as st
from utils.login import login

st.set_page_config(page_title="Pulseritas Co", layout="centered")

# Llamamos a la función login. Esta función:
# - Muestra el formulario si no estás logueada
# - Guarda el estado y rerun si sí estás logueada
login()

# Si el login fue exitoso, esta parte ya se ejecuta en el "segundo intento"
st.sidebar.title("📁 Navegación")
st.sidebar.success("Selecciona una página a la izquierda ☝️")
