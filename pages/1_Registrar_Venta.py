# pages/1_Registrar_Venta.py
import streamlit as st
import pandas as pd
from datetime import datetime
import os
import config
from utils import auth

# --- Protección de la Página ---
# Esta línea es clave. Si no se ha iniciado sesión, detiene la ejecución.
auth.proteger_pagina()
auth.mostrar_logout() # Muestra el botón de logout en la barra lateral

# --- Contenido de la Página ---
st.title("🛍️ Registrar una Venta")
st.write("¡Aquí es donde sucede la magia! Registra cada pulsera vendida.")

# Usamos un formulario para agrupar los inputs y el botón
with st.form("venta_form", clear_on_submit=True):
    # Usamos las llaves del diccionario de pulseras para las opciones
    tipo_pulsera = st.selectbox("Selecciona el tipo de pulsera", options=list(config.PULSERAS.keys()))
    cantidad = st.number_input("¿Cuántas vendiste?", min_value=1, step=1, value=1)
    
    # Botón para enviar el formulario
    submitted = st.form_submit_button("Registrar Venta")

    if submitted:
        # Buscamos la información de la pulsera en nuestro archivo de configuración
        info_pulsera = config.PULSERAS[tipo_pulsera]
        
        # Calculamos los montos
        monto_desayuno = cantidad * info_pulsera["desayuno"]
        monto_reinversion = cantidad * info_pulsera["reinversion"]

        nueva_venta = {
            "fecha": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            "vendedor": [st.session_state.usuario],
            "tipo": [tipo_pulsera],
            "cantidad": [cantidad],
            "desayuno_soles": [monto_desayuno],
            "reinversion_soles": [monto_reinversion]
        }
        df_nueva_venta = pd.DataFrame(nueva_venta)

        # Lógica para guardar en el CSV
        try:
            if os.path.exists(config.ARCHIVO_VENTAS):
                df_existente = pd.read_csv(config.ARCHIVO_VENTAS)
                df_final = pd.concat([df_existente, df_nueva_venta], ignore_index=True)
            else:
                df_final = df_nueva_venta
            
            df_final.to_csv(config.ARCHIVO_VENTAS, index=False)

            # Mensajes de éxito
            st.success(f"✅ ¡Venta registrada! Se añadieron:")
            st.info(f"🥐 S/ {monto_desayuno:.2f} para desayunos.")
            st.info(f"💰 S/ {monto_reinversion:.2f} para el fondo de reinversión.")

        except Exception as e:
            st.error(f"Ocurrió un error al guardar la venta: {e}")
