import streamlit as st

# Diccionario de usuarios válidos
USUARIOS = {
    "linda": "pulseritas123",
    "daira": "pulseritas456"
}

# Estado de sesión
if "logueado" not in st.session_state:
    st.session_state.logueado = False
if "usuario" not in st.session_state:
    st.session_state.usuario = ""

# Si no está logueado, mostrar login
if not st.session_state.logueado:
    st.title("💖 Bienvenida a Pulseritas Co 💖")
    st.subheader("Inicia sesión para entrar a la magia ✨")

    usuario = st.text_input("👩‍💻 Usuario").lower()
    contraseña = st.text_input("🔑 Contraseña", type="password")

    if st.button("Entrar"):
        if usuario in USUARIOS and USUARIOS[usuario] == contraseña:
            st.session_state.logueado = True
            st.session_state.usuario = usuario
            st.success("Inicio de sesión exitoso ✨ Redirigiendo...")
            st.stop()  # ⛔ Para aquí, y la próxima vez ya entra al contenido
        else:
            st.error("Usuario o contraseña incorrectos 💔")

else:
    # Si ya está logueado, mostrar la app completa
    st.sidebar.title("Menú 💖")
    page = st.sidebar.radio("Ir a:", ["Inicio", "Reporte de Ventas", "Métricas", "Cerrar sesión"])

    st.title(f"¡Hola, {st.session_state.usuario.capitalize()}! 💗✨")

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
