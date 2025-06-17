import streamlit as st

def main():
    usuario = st.session_state.get("usuario", "amiga")
    st.title(f"¡Hola, {usuario.capitalize()}! 🌈✨")
    st.write("Esta es nuestra app para reportar ventas, ver métricas y seguir alimentando sonrisas.")
    st.write("Usa el menú lateral para navegar. 🧵🪡")

if __name__ == "__main__":
    main()
