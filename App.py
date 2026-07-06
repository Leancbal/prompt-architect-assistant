import streamlit as st

def main():
    # Define the pages
    page_1 = st.Page("page_1.py", title="Bienvenidos!", icon="📖")
    page_2 = st.Page("page_2.py", title="Información", icon="📚")
    page_3 = st.Page("page_3.py", title="Prompt Architect Assistant", icon="🛠️")

    # Set up navigation
    pg = st.navigation([page_1, page_2, page_3])

    # Run the selected page
    pg.run()

main()