import streamlit as st
from utils.login import login

# Inicializa sesión si no existe
if "logueado" not in st.session_state:
    st.session_state.logueado = False
if "usuario" not in st.session_state:
    st.session_state.usuario = ""

# Si no está logueado, mostramos pantalla de login
if not st.session_state.logueado:
    success, usuario = login()
    if success:
        st.session_state.logueado = True
        st.session_state.usuario = usuario
        st.experimental_rerun()
else:
    # Menú lateral
    st.sidebar.title("Menú 💖")
    page = st.sidebar.radio("Ir a:", ["Inicio", "Reporte de Ventas", "Métricas", "Cerrar sesión"])

    # Página principal
    st.title(f"¡Hola, {st.session_state.usuario.capitalize()}! 🌈✨")

    if page == "Inicio":
        st.markdown("""
        Esta es nuestra app para reportar ventas, ver métricas y seguir alimentando sonrisas.  
        Usa el menú lateral para navegar. 🧵🪡
        """)
    
    elif page == "Reporte de Ventas":
        st.subheader("🧾 Reporte de Ventas")
        st.write("Aquí irán los formularios para registrar tus ventas.")
    
    elif page == "Métricas":
        st.subheader("📊 Métricas")
        st.write("Aquí verás datos de tus ventas, desayunos entregados y más.")
    
    elif page == "Cerrar sesión":
        st.session_state.logueado = False
        st.session_state.usuario = ""
        st.experimental_rerun()
