import streamlit as st
from utils.login import login

# Inicializar estados de sesión si no existen
if "logueado" not in st.session_state:
    st.session_state.logueado = False
if "usuario" not in st.session_state:
    st.session_state.usuario = ""

# Login
if not st.session_state.logueado:
    st.title("💖 Bienvenida a Pulseritas Co 💖")
    st.subheader("Inicia sesión para entrar a la magia ✨")

    usuario = st.text_input("👩‍💻 Usuario").lower()
    contraseña = st.text_input("🔑 Contraseña", type="password")

    if st.button("Entrar"):
        if login(usuario, contraseña):
            st.session_state.logueado = True
            st.session_state.usuario = usuario
            st.success("Inicio de sesión exitoso ✨ Redirigiendo...")
            st.experimental_rerun()
        else:
            st.error("Usuario o contraseña incorrectos 💔")

# Si ya está logueado, mostrar bienvenida general
else:
    st.sidebar.title("Menú 💖")
    st.sidebar.success("Usa el menú para navegar por la app.")
    st.title(f"¡Hola, {st.session_state.usuario.capitalize()}! 🌈✨")
    st.markdown("""
    Esta es nuestra app para reportar ventas, ver métricas y seguir alimentando sonrisas.  
    Usa el menú lateral para navegar. 🧵🪡
    """)
