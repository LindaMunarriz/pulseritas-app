import streamlit as st

if 'logueado' not in st.session_state or not st.session_state.logueado:
    st.warning("Por favor, inicia sesión para acceder.")
    st.stop()

st.title("🏠 Inicio")
st.write(f"¡Bienvenida, {st.session_state.usuario.capitalize()}! 🌈✨")
st.write("Esta es la página de inicio. Usa el menú lateral para navegar por la app. 💖")
