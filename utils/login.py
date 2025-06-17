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

    login_clicado = st.button("Entrar")

    if login_clicado:
        if usuario in USUARIOS and USUARIOS[usuario] == contraseña:
            return True, usuario
        else:
            st.error("Usuario o contraseña incorrectos 💔")
            return False, ""
    return False, ""
