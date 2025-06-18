import streamlit as st
from utils.login import login

# Inicializamos variables de sesión
if "logueado" not in st.session_state:
    st.session_state.logueado = False

# Login
if not st.session_state.logueado:
    login()
else:
    st.sidebar.success(f"✨ ¡Bienvenida, {st.session_state.usuario}!")
