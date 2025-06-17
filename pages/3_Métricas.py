import streamlit as st

if 'logueado' not in st.session_state or not st.session_state.logueado:
    st.warning("Por favor, inicia sesión para acceder.")
    st.stop()

st.title("📊 Métricas")
st.write("Aquí podrás ver estadísticas y métricas de tus ventas. 📈")

# Ejemplo de métrica visual (mock)
st.metric("Ventas esta semana", "12", "+3")
st.metric("Total recaudado", "$245", "+$50")
