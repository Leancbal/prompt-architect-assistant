import streamlit as st

# Descripciones de contenido de pagina en barra lateral.
st.sidebar.markdown("# Contenido:\n"
                    "### - Introducción\n"
                    "### - Componentes\n"
                    "### - Ejemplos\n"
                    "### - Técnicas de prompting\n"
                    "### - Concejos")

# Apertura y lectura de archivo .md que importa el contenido de la pagina - primera parte.
with open("archivos/markdown_prompts.md", "r", encoding="utf-8") as markdown:
    contenido = markdown.read()

st.markdown(contenido)

# Carga de imagen informativa que se ejecuta entre los archivos .md para que pueda ser importada directamente.
st.image("archivos/image.png", caption="Componentes de un buen prompt", use_container_width= True)

# Apertura y lectura de archivo .md que importa el contenido de la pagina - segunda parte.
with open("archivos/markdown_prompts2.md", "r", encoding="utf-8") as markdown2:
    contenido2= markdown2.read()

st.markdown(contenido2)

# Texto con hipervinculo que redirige a blog informativo.
st.write("""##### [`Mas información`](https://www.inavirtual.ed.cr/pluginfile.php/2974270/mod_resource/content/16/index.html)""")