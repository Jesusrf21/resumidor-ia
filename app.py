import streamlit as st
import fitz  # PyMuPDF
from transformers import (
    pipeline,
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
)

# Cargar un modelo de resumen que soporte español
@st.cache_resource
def load_summarizer():
    """Carga el modelo multilingüe y su tokenizer en modo lento.

    Usamos `use_fast=False` para evitar errores de conversión cuando no está
    disponible el tokenizer rápido.
    """
    model_name = "csebuetnlp/mT5_multilingual_XLSum"
    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return pipeline("summarization", model=model, tokenizer=tokenizer)

summarizer = load_summarizer()

# Función para extraer texto del PDF
def extract_text_from_pdf(file):
    text = ""
    with fitz.open(stream=file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

# Función para dividir texto en bloques (el modelo tiene un límite de tokens)
def split_text(text, max_chars=1000):
    return [text[i:i+max_chars] for i in range(0, len(text), max_chars)]

# Función para resumir texto completo con parámetros dinámicos
def summarize_text(full_text, resumen_params):
    blocks = split_text(full_text)
    summaries = []
    for i, block in enumerate(blocks):
        st.info(f"Resumiendo bloque {i + 1} de {len(blocks)}...")
        summary = summarizer(block, **resumen_params, do_sample=False)[0]['summary_text']
        summaries.append(summary)
    return "\n\n".join(summaries)

# Interfaz de usuario
st.title("📄 Resumidor de PDFs con IA gratuita (HuggingFace)")

uploaded_file = st.file_uploader("Sube un archivo PDF", type="pdf")

if uploaded_file:
    with st.spinner("Extrayendo texto del PDF..."):
        full_text = extract_text_from_pdf(uploaded_file)

    st.subheader("Texto extraído:")
    with st.expander("Mostrar/Ocultar texto"):
        st.write(full_text[:3000] + "..." if len(full_text) > 3000 else full_text)

    # NUEVO BLOQUE: Selector de longitud del resumen
    st.subheader("🛠️ Ajustes del resumen")
    resumen_largo = st.selectbox(
        "Selecciona la longitud del resumen",
        ("Breve (≈50 palabras)", "Medio (≈100 palabras)", "Detallado (≈150 palabras)")
    )

    # Mapear la selección a parámetros reales del modelo
    if resumen_largo == "Breve (≈50 palabras)":
        resumen_params = {"min_length": 20, "max_length": 60}
    elif resumen_largo == "Medio (≈100 palabras)":
        resumen_params = {"min_length": 50, "max_length": 120}
    else:
        resumen_params = {"min_length": 80, "max_length": 180}

    if st.button("🔍 Generar resumen"):
        with st.spinner("Resumiendo..."):
            resumen_final = summarize_text(full_text, resumen_params)
            st.subheader("🧠 Resumen generado:")
            st.text_area("Resumen:", resumen_final, height=400)
