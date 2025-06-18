import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.title("🛍️ Reporte de Ventas")

# Diccionario con precios y destinos
PULSERAS = {
    "corazon": {"precio": 2, "desayuno": 1.5, "reinversion": 0.5},
    "power": {"precio": 3, "desayuno": 3.0, "reinversion": 0.0}
}

tipo = st.selectbox("Selecciona el tipo de pulsera", ["corazon", "power"])
cantidad = st.number_input("¿Cuántas vendiste?", min_value=1, step=1)

if st.button("Registrar venta"):
    data = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tipo": tipo,
        "cantidad": cantidad,
        "desayuno": cantidad * PULSERAS[tipo]["desayuno"],
        "reinversion": cantidad * PULSERAS[tipo]["reinversion"]
    }

    archivo = "ventas.csv"
    df = pd.DataFrame([data])

    if os.path.exists(archivo):
        df_existente = pd.read_csv(archivo)
        df = pd.concat([df_existente, df], ignore_index=True)

    df.to_csv(archivo, index=False)
    st.success(f"✅ Venta registrada: {cantidad} pulseras '{tipo}'")
    st.info(f"🥐 {data['desayuno']:.2f} soles para desayunos")
    st.info(f"💰 {data['reinversion']:.2f} soles para el fondo de reinversión")
