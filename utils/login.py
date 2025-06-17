import streamlit as st
# La siguiente línea es nueva, para poder cambiar de página
from streamlit.runtime.scriptrunner import get_script_run_ctx

# Diccionario de usuarios válidos
USUARIOS = {
    "linda": "pulseritas123",
    "daira": "pulseras456"
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
            
            # NOTA: He quitado el st.success y el st.rerun()
            # Ahora los reemplazamos por esta línea mágica:
            st.switch_page("pages/1_Inicio.py")
            
        else:
            st.error("Usuario o contraseña incorrectos 💔")
