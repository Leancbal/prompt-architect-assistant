import streamlit as st

# Main page content
st.markdown("# 🧠 Prompt Architect Assistant")
st.write("---")
st.sidebar.markdown("# Introdución")

with open("archivos/markdown_prompts3.md", "r", encoding="utf-8") as markdown:
 contenido3 = markdown.read()

st.markdown(contenido3)