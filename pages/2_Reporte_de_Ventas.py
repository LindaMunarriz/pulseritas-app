import streamlit as st

if 'logueado' not in st.session_state or not st.session_state.logueado:
    st.warning("Por favor, inicia sesión para acceder.")
    st.stop()

st.title("🧾 Reporte de Ventas")
st.write("Aquí irán los formularios para registrar tus ventas.")

# Ejemplo de formulario
with st.form("form_venta"):
    producto = st.text_input("Producto vendido")
    cantidad = st.number_input("Cantidad", min_value=1, step=1)
    enviado = st.form_submit_button("Registrar")

    if enviado:
        st.success(f"Venta registrada: {producto} x{cantidad}")
