# utils/auth.py
import streamlit as st

def proteger_pagina():
    """
    Verifica si el usuario está logueado. Si no, lo detiene
    y le pide que inicie sesión.
    Esta función se debe llamar al inicio de cada página protegida.
    """
    if not st.session_state.get("logueado", False):
        st.warning("🤫 Debes iniciar sesión para ver esta página.")
        st.stop() # Detiene la ejecución de la página actual

def mostrar_logout():
    """Añade un botón de logout a la barra lateral."""
    if st.sidebar.button("Salir de la cuenta 🚪"):
        # Limpiamos todo el estado de la sesión
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        # Forzamos un rerun para que pida el login de nuevo
        st.rerun()
