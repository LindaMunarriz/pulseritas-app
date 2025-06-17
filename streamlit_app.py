import streamlit as st
from datetime import datetime
import pandas as pd

# --- Configuración de la página ---
st.set_page_config(page_title="Pulseritas Co", page_icon="🎀")

# --- Usuarios permitidos ---
USERS = {
    "linda": "pulseritas123",
    "daira": "pulseritas456"
}

# --- Autenticación ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    st.title("💖 Bienvenida a Pulseritas Co 💖")
    st.markdown("Inicia sesión para entrar a la magia ✨")

    username = st.text_input("👩‍💻 Usuario")
    password = st.text_input("🔑 Contraseña", type="password")

    if st.button("Iniciar sesión"):
        if username.lower() in USERS and USERS[username.lower()] == password:
            st.success(f"¡Hola, {username.capitalize()}! 🌈✨")
            st.session_state.authenticated = True
            st.session_state.username = username.capitalize()
            st.experimental_rerun()
        else:
            st.error("Usuario o contraseña incorrectos 💔")

    st.stop()

# --- Sidebar con nombre del usuario ---
st.sidebar.title("🧵 Pulseritas Co")
st.sidebar.markdown(f"👑 Logueada como: **{st.session_state.username}**")

opcion = st.sidebar.radio("Selecciona una opción", [
    "Inicio",
    "Registrar Venta",
    "Registrar Compra de Desayuno",
    "Ver Resumen Financiero",
    "Ver Gráfico de Ventas",
    "Salir"
])

# --- DataFrame en memoria ---
if "ventas" not in st.session_state:
    st.session_state.ventas = pd.DataFrame(columns=["fecha", "tipo", "cantidad", "total", "a_desayuno", "a_reinversion"])

# --- Contenido por sección ---
if opcion == "Inicio":
    st.title("Bienvenida a Pulseritas Co. 🧵✨")
    st.markdown("""
    ¡Hola linda! 💗 Esta es nuestra app para reportar ventas, ver métricas y seguir alimentando sonrisas.

    Selecciona una opción del menú lateral 👈
    """)

elif opcion == "Registrar Venta":
    st.title("Registrar Venta 🧾")

    tipo = st.radio("¿Qué tipo de pulserita vendiste?", ["💗 Corazón (S/ 2.00)", "💪 Power (S/ 3.00)"])
    cantidad = st.number_input("¿Cuántas vendiste?", min_value=1, step=1)
    fecha = st.date_input("Fecha de la venta", value=datetime.today())

    if st.button("Registrar"):
        if "Corazón" in tipo:
            precio = 2.00
            a_desayuno = 1.00 * cantidad
            a_reinversion = 1.00 * cantidad
        else:
            precio = 3.00
            a_desayuno = 2.00 * cantidad
            a_reinversion = 1.00 * cantidad

        total = precio * cantidad

        st.session_state.ventas.loc[len(st.session_state.ventas)] = {
            "fecha": fecha,
            "tipo": tipo,
            "cantidad": cantidad,
            "total": total,
            "a_desayuno": a_desayuno,
            "a_reinversion": a_reinversion
        }

        desayunos = int(a_desayuno // 3)
        st.success(f"🎉 ¡Venta registrada! Total: S/ {total:.2f}")
        st.info(f"🍞 {desayunos} desayunos posibles • 💎 S/ {a_reinversion:.2f} reinvertidos")

elif opcion == "Registrar Compra de Desayuno":
    st.title("🍞 Registrar Compra de Desayuno")
    st.write("💡 Esta parte la haremos después 😉")

elif opcion == "Ver Resumen Financiero":
    st.title("💰 Resumen Financiero")
    if st.session_state.ventas.empty:
        st.warning("No hay datos aún.")
    else:
        total = st.session_state.ventas["total"].sum()
        fondo_desayuno = st.session_state.ventas["a_desayuno"].sum()
        fondo_reinv = st.session_state.ventas["a_reinversion"].sum()
        desayunos = int(fondo_desayuno // 3)

        st.metric("Total vendido", f"S/ {total:.2f}")
        st.metric("Fondos para desayuno", f"S/ {fondo_desayuno:.2f} ({desayunos} desayunos)")
        st.metric("Fondos para reinversión", f"S/ {fondo_reinv:.2f}")

elif opcion == "Ver Gráfico de Ventas":
    st.title("📈 Gráfico de Ventas")
    if st.session_state.ventas.empty:
        st.warning("Aún no hay ventas registradas.")
    else:
        ventas_por_dia = st.session_state.ventas.groupby("fecha")["total"].sum().reset_index()
        st.bar_chart(ventas_por_dia.set_index("fecha"))

else:
    st.title("¡Hasta pronto! 💗")
    st.balloons()
