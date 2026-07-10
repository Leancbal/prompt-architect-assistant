import streamlit as st

st.markdown("# 🧠 Prompt Maker")
st.write("---")

# Apertura y lectura de archivo .md que importa el contenido de la pagina
with open("archivos/markdown_prompts3.md", "r", encoding="utf-8") as markdown:
 contenido3 = markdown.read()

st.markdown(contenido3)