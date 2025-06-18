import streamlit as st
import pandas as pd
import os

st.title("📊 Métricas y Fondos")

archivo = "ventas.csv"

if os.path.exists(archivo):
    df = pd.read_csv(archivo)

    total_desayunos_soles = df["desayuno"].sum()
    total_reinversion = df["reinversion"].sum()
    total_ventas = df["cantidad"].sum()
    total_transacciones = len(df)
    desayunos_estimados = int(total_desayunos_soles // 3)

    st.metric("💸 Total en desayunos (S/)", f"{total_desayunos_soles:.2f}")
    st.metric("💰 Fondo de reinversión (S/)", f"{total_reinversion:.2f}")
    st.metric("🥐 Desayunos posibles", f"{desayunos_estimados}")
    st.metric("🧾 Ventas registradas", total_transacciones)
    st.metric("🛍️ Pulseras vendidas", total_ventas)

    with st.expander("Ver historial de ventas"):
        st.dataframe(df)
else:
    st.warning("No hay ventas registradas todavía.")
