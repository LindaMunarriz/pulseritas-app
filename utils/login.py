# utils/login.py
import streamlit as st

# Diccionario de usuarios válidos
USUARIOS = {
    "linda": "pulseritas123",
    "daira": "pulseritas456"
}

def login():
    st.title("💖 Bienvenida a Pulseritas Co 💖")
    st.subheader("Inicia sesión para entrar a la magia ✨")

    usuario = st.text_input("👩‍💻 Usuario").lower()
    contraseña = st.text_input("🔑 Contraseña", type="password")

    if st.button("Entrar"):
        if usuario in USUARIOS and USUARIOS[usuario] == contraseña:
            st.session_state.logueado = True
            st.session_state.usuario = usuario
            
            # <-- CAMBIO CLAVE: Redirigimos a la página de inicio usando solo el nombre del archivo
            st.switch_page("1_Inicio.py")
            
        else:
            st.error("Usuario o contraseña incorrectos 💔")
