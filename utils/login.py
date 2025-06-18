# utils/login.py
import streamlit as st

USUARIOS = {
    "linda": "pulseritas123",
    "daira": "pulseritas456"
}

def check_login():
    """Verifica si el usuario ya está logueado"""
    return st.session_state.get("logueado", False)

def login():
    """Renderiza el formulario de login y guarda sesión si es exitoso"""
    if check_login():
        return

    st.title("💖 Bienvenida a Pulseritas Co 💖")
    st.subheader("Inicia sesión para entrar a la magia ✨")

    usuario = st.text_input("👩‍💻 Usuario").lower()
    contraseña = st.text_input("🔑 Contraseña", type="password")

    if st.button("Entrar"):
        if usuario in USUARIOS and USUARIOS[usuario] == contraseña:
            st.session_state.logueado = True
            st.session_state.usuario = usuario
            st.success("Inicio de sesión exitoso ✨ ¡Bienvenida!")
            st.experimental_rerun()
        else:
            st.error("Usuario o contraseña incorrectos 💔")
