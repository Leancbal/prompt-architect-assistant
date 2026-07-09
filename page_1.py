import streamlit as st

# Contenido de pagina 1 (Titulo y descripcion en barra lateral)
st.markdown("# 🧠 Prompt Maker")
st.write("---")
st.sidebar.markdown("# Introdución")

# Apertura y lectura de archivo .md que importa el contenido de la pagina
with open("archivos/markdown_prompts3.md", "r", encoding="utf-8") as markdown:
 contenido3 = markdown.read()

st.markdown(contenido3)