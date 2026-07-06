import streamlit as st

st.sidebar.markdown("# Contenido:\n"
                    "### - Introduccion\n"
                    "### - Componentes\n"
                    "### - Ejemplos\n"
                    "### - Tecnicas de prompting\n"
                    "### - Concejos")

with open("archivos/markdown_prompts.md", "r", encoding="utf-8") as markdown:
    contenido = markdown.read()

st.markdown(contenido)

st.image("archivos/image.png", caption="Componentes de un buen prompt", use_container_width= True)

with open("archivos/markdown_prompts2.md", "r", encoding="utf-8") as markdown2:
    contenido2= markdown2.read()

st.markdown(contenido2)

st.write("""##### [`Mas información`](https://www.inavirtual.ed.cr/pluginfile.php/2974270/mod_resource/content/16/index.html)""")