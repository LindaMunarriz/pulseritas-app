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
            st.success("Inicio de sesión exitoso ✨ Redirigiendo...")
            st.experimental_rerun()
        else:
            st.error("Usuario o contraseña incorrectos 💔")
