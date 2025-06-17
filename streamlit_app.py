import streamlit as st
from utils.login import login

# Inicializar sesión si no existe
if "logueado" not in st.session_state:
    st.session_state.logueado = False

# Si no está logueado, mostrar login
if not st.session_state.logueado:
    login()
else:
    st.sidebar.success(f"¡Hola, {st.session_state.usuario.capitalize()}! 🌈✨")
    st.write(f"## ¡Hola, {st.session_state.usuario.capitalize()}! 🌈✨")
    st.write("""
    Esta es nuestra app para reportar ventas, ver métricas y seguir alimentando sonrisas.
    Usa el menú lateral para navegar. 🧵🪡
    """)

    # Página de inicio provisional
    st.header("🧾 Reporte de Ventas")
    st.info("Aquí irán los formularios para registrar tus ventas.")
