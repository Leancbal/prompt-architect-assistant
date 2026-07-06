import streamlit as st

st.title("🧠 Prompt Architect Assistant")
st.write(
    "Construye prompts profesionales mediante esta guía paso a paso."
)

if "paso" not in st.session_state:
    st.session_state.paso = 1

if st.session_state.paso == 1:

    st.subheader("Paso 1: Objetivo")

    objetivo = st.text_area(
        "¿Qué deseas lograr con este prompt?"
    )

    if st.button("Siguiente"):
        st.session_state.objetivo = objetivo
        st.session_state.paso = 2
        st.rerun()

elif st.session_state.paso == 2:

    st.subheader("Paso 2: Contexto")

    contexto = st.text_area(
        "¿Qué información necesita conocer la IA?"
    )

    if st.button("Siguiente"):
        st.session_state.contexto = contexto
        st.session_state.paso = 3
        st.rerun()

elif st.session_state.paso == 3:

    st.subheader("Paso 3: Rol")

    rol = st.text_area(
        "¿Qué rol debe tomar la IA?"
    )

    if st.button("Siguiente"):
        st.session_state.rol = rol
        st.session_state.paso = 4
        st.rerun()

elif st.session_state.paso == 4:

    st.subheader("Paso 4: Tareas")

    tareas = st.text_area(
        "Describe las tareas o pasos que debe realizar la IA."
    )

    if st.button("Siguiente"):
        st.session_state.tareas = tareas
        st.session_state.paso = 5
        st.rerun()

elif st.session_state.paso == 5:

    st.subheader("Paso 5: Reglas")

    reglas = st.text_area(
        "Indica restricciones o reglas."
    )

    if st.button("Siguiente"):
        st.session_state.reglas = reglas
        st.session_state.paso = 6
        st.rerun()

elif st.session_state.paso == 6:

    st.subheader("Paso 6: Salida esperada")

    salida = st.text_area(
        "Indica el formato del contenido (resumen/imagen o JSON/Dataframe)."
    )

    if st.button("Siguiente"):
        st.session_state.salida = salida
        st.session_state.paso = 7
        st.rerun()

elif st.session_state.paso == 7:

    st.subheader("Paso 7: Técnicas de Prompting")

    tecnica = st.selectbox(
        "¿Deseas aplicar una técnica?",
        [
            "Ninguna",
            "Few-Shot Prompting",
            "Zero-Shot Prompting",
            "Chain of Thought",
            "Role Prompting",
            "Structured Output"
        ]
    )

    if tecnica == "Few-Shot Prompting":
        st.info(
            """
            Few-Shot Prompting:
            Proporciona ejemplos para guiar la respuesta.
            Ideal para clasificación y generación consistente.
            """
        )

    if tecnica == "Zero-Shot Prompting":
        st.info(
            """
            Zero-Shot Prompting:
            Aumenta la claridad y detalle en las tareas.
            """
        )


    elif tecnica == "Chain of Thought":
        st.info(
            """
            Chain of Thought:
            Solicita razonamiento paso a paso.
            Ideal para problemas complejos.
            """
        )

    elif tecnica == "Role Prompting":
        st.info(
            """
            Role Prompting:
            Refuerza el rol especializado.
            """
        )

    elif tecnica == "Structured Output":
        st.info(
            """
            Structured Output:
            Obliga a responder con una estructura definida.
            """
        )

    if st.button("Generar Prompt"):
        st.session_state.tecnica = tecnica
        st.session_state.paso = 8
        st.rerun()

elif st.session_state.paso == 8:

    prompt = f"""
            ACTÚA COMO:
            {st.session_state.rol}
            
            OBJETIVO:
            {st.session_state.objetivo}
            
            CONTEXTO:
            {st.session_state.contexto}
            
            TAREAS:
            {st.session_state.tareas}
            
            REGLAS:
            {st.session_state.reglas}
            
            FORMATO DE SALIDA:
            {st.session_state.salida}
            """

    tecnica = st.session_state.tecnica

    if tecnica == "Chain of Thought":

        prompt += """

            INSTRUCCIÓN ADICIONAL:
            Piensa paso a paso antes de responder.
            Explica tu razonamiento de manera lógica y estructurada.
            """

    elif tecnica == "Few-Shot Prompting":

        prompt += """
                
            INSTRUCCIÓN ADICIONAL:
            Antes de resolver la tarea,
            genera ejemplos representativos
            y utilízalos como referencia.
            """

    elif tecnica == "Zero-Shot Prompting":

        prompt += """
                
            INSTRUCCIÓN ADICIONAL:
            Analiza y detalla profundamente
            cada tarea.
            """

    elif tecnica == "Role Prompting":

        prompt += """

            INSTRUCCIÓN ADICIONAL:
            Mantén el rol profesional durante toda la respuesta.
            """

    elif tecnica == "Structured Output":

        prompt += """

            INSTRUCCIÓN ADICIONAL:
            Devuelve la información utilizando una estructura clara,
            con títulos y subtítulos bien definidos.
            """

    st.success("Prompt generado correctamente")

    st.code(
        prompt,
        language="markdown"
    )

    if st.button("Crear nuevo prompt"):

        for key in list(st.session_state.keys()):
            del st.session_state[key]

        st.rerun()