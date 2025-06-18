# utils/login.py
import streamlit as st

USUARIOS = {
    "linda": "pulseritas123",
    "daira": "pulseritas456"
}

def check_login():
    return st.session_state.get("logueado", False)

def login():
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
        else:
            st.error("Usuario o contraseña incorrectos 💔")
