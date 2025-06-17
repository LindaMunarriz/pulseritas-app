import streamlit as st
from utils.login import login

# Inicializar variables de sesión
if 'logueado' not in st.session_state:
    st.session_state.logueado = False
if 'usuario' not in st.session_state:
    st.session_state.usuario = ''

# Mostrar login o bienvenida
if not st.session_state.logueado:
    login()
else:
    st.success(f"¡Hola, {st.session_state.usuario.capitalize()}! 🌈✨")
    st.write("Esta es nuestra app para reportar ventas, ver métricas y seguir alimentando sonrisas.")
    st.write("Usa el menú lateral para navegar. 🧵🪡")
