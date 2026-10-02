import os
import streamlit as st
from google import genai

st.set_page_config(
    page_title="Prueba Gemini",
    page_icon="🧪"
)

st.title("Prueba de conexión con Gemini")

api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.error("Falta GEMINI_API_KEY en los Secrets de Streamlit.")
    st.stop()

if st.button("Probar Gemini", type="primary"):
    with st.spinner("Probando conexión..."):

        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-3.7-flash",
            contents="Escribe una frase breve sobre el agua en Bioquímica."
        )

        st.write(response.text)
