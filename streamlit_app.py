import streamlit as st

st.set_page_config(page_title="Pulseritas Co", page_icon="🧿")

st.sidebar.title("Menú 💖")
page = st.sidebar.radio("Ir a:", ["Inicio", "Reporte de Ventas", "Métricas"])

if page == "Inicio":
    st.title("Bienvenida a Pulseritas Co. 🧵✨")
    st.markdown("""
    ¡Hola linda! 💗 Esta es nuestra app para reportar ventas, ver métricas y seguir alimentando sonrisas.

    Selecciona una opción del menú lateral 👈
    """)
elif page == "Reporte de Ventas":
    st.title("Reporte de Ventas 🧾")
    st.write("Aquí irán los formularios para registrar tus ventas.")
elif page == "Métricas":
    st.title("Métricas 📊")
    st.write("Aquí verás datos de tus ventas, desayunos entregados y más.")
