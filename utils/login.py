# utils/login.py
import streamlit as st
import config # Importamos nuestra configuración central

def mostrar_login():
    """Muestra el formulario de inicio de sesión."""
    st.title("💖 Bienvenida a Pulseritas Co 💖")
    st.subheader("Inicia sesión para entrar a la magia ✨")

    with st.form("login_form"):
        usuario = st.text_input("👩‍💻 Usuario").lower()
        contraseña = st.text_input("🔑 Contraseña", type="password")
        submitted = st.form_submit_button("Entrar")

        if submitted:
            # Validamos las credenciales usando el diccionario de config.py
            if usuario in config.USUARIOS and config.USUARIOS[usuario] == contraseña:
                st.session_state.logueado = True
                st.session_state.usuario = usuario
                
                # Redirigimos a la primera página funcional.
                # Nota: solo se usa el nombre del archivo, Streamlit ya sabe que está en /pages
                st.switch_page("pages/1_Registrar_Venta.py")
            else:
                st.error("Usuario o contraseña incorrectos 💔")
