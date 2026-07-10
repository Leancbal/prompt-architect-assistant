import streamlit as st

def main():
    # Definicion de paginas
    page_1 = st.Page("page_1.py", title="Proyecto", icon="📖")
    page_2 = st.Page("page_2.py", title="Información", icon="📚")
    page_3 = st.Page("page_3.py", title="Prompt Maker", icon="🛠️")

    # Navegacion de paginas
    pg = st.navigation([page_3, page_2, page_1])

    # Ejecuta la pagina seleccionada
    pg.run()

main()