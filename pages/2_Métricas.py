# pages/2_Métricas.py
import streamlit as st
import pandas as pd
import os
import config
from utils import auth

# --- Protección de la Página ---
auth.proteger_pagina()
auth.mostrar_logout()

# --- Contenido de la Página ---
st.title("📊 Métricas y Fondos Acumulados")

if not os.path.exists(config.ARCHIVO_VENTAS):
    st.warning("Aún no hay ventas registradas. ¡Ve a 'Registrar Venta' para empezar!")
    st.stop()

# Leer los datos del CSV
try:
    df = pd.read_csv(config.ARCHIVO_VENTAS)

    if df.empty:
        st.info("El archivo de ventas está vacío.")
        st.stop()

    # --- Cálculos ---
    total_desayunos_soles = df["desayuno_soles"].sum()
    total_reinversion = df["reinversion_soles"].sum()
    total_pulseras_vendidas = df["cantidad"].sum()
    total_transacciones = len(df)
    
    # Usamos la constante del archivo de config
    desayunos_posibles = int(total_desayunos_soles // config.COSTO_POR_DESAYUNO)

    # --- Mostrar Métricas ---
    st.header("Resumen General 📈")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("🥐 Desayunos Posibles", f"{desayunos_posibles}")
    col2.metric("💸 Total para Desayunos", f"S/ {total_desayunos_soles:.2f}")
    col3.metric("💰 Fondo de Reinversión", f"S/ {total_reinversion:.2f}")

    col4, col5 = st.columns(2)
    col4.metric("🛍️ Total Pulseras Vendidas", f"{total_pulseras_vendidas}")
    col5.metric("🧾 Total de Ventas (Transacciones)", f"{total_transacciones}")
    
    st.divider()

    # --- Detalle de Ventas ---
    st.header("Historial de Ventas 📋")
    
    # Para mejorar la visualización, podemos renombrar las columnas
    df_display = df.rename(columns={
        "fecha": "Fecha y Hora",
        "vendedor": "Vendedor(a)",
        "tipo": "Tipo de Pulsera",
        "cantidad": "Cantidad",
        "desayuno_soles": "Aporte Desayuno (S/)",
        "reinversion_soles": "Aporte Reinversión (S/)"
    })
    
    st.dataframe(df_display, use_container_width=True)

except Exception as e:
    st.error(f"No se pudo leer el archivo de ventas: {e}")
