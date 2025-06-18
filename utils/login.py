import streamlit as st

USUARIOS = {
    "linda": "pulseritas123",
    "daira": "pulseritas456"
}

def login():
    if "logueado" not in st.session_state:
        st.session_state.logueado = False

    if not st.session_state.logueado:
        st.title("💖 Bienvenida a Pulseritas Co 💖")
        st.subheader("Inicia sesión para entrar a la magia ✨")
        usuario = st.text_input("👩‍💻 Usuario").lower()
        contraseña = st.text_input("🔑 Contraseña", type="password")
        login_button = st.button("Entrar")

        if login_button:
            if usuario in USUARIOS and USUARIOS[usuario] == contraseña:
                st.session_state.logueado = True
                st.session_state.usuario = usuario
                st.success("Inicio de sesión exitoso ✨ ¡Bienvenida!")
            else:
                st.error("Usuario o contraseña incorrectos 💔")
        st.stop()
