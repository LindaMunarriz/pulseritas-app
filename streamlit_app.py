# streamlit_app.py
import streamlit as st
from utils import login, auth

# Configuración de la página (título, ícono)
st.set_page_config(
    page_title="Pulseritas Co",
    page_icon="💖"
)

# Inicializa el estado de la sesión si no existe
if "logueado" not in st.session_state:
    st.session_state.logueado = False

# Muestra el formulario de login si el usuario no está autenticado
if not st.session_state.logueado:
    login.mostrar_login()
else:
    # Si el usuario ya está logueado, muestra la bienvenida y el botón de logout
    st.sidebar.success(f"✨ ¡Bienvenida, {st.session_state.usuario}!")
    
    st.title("💖 Bienvenida a Pulseritas Co 💖")
    st.write("Usa el menú de la izquierda para navegar entre las páginas.")
    st.info("👈 Selecciona **'Registrar Venta'** para empezar.")
    
    auth.mostrar_logout()

