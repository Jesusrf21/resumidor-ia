# Resumidor de PDFs con IA

Una aplicación en Python + Streamlit que resume automáticamente documentos PDF utilizando modelos gratuitos de Hugging Face.

La aplicación emplea el modelo `csebuetnlp/mT5_multilingual_XLSum`, capaz de generar resúmenes en español.

## Cómo usar

1. Crea un entorno virtual y activa:
   ```
   python -m venv venv
   source venv/bin/activate  # o .\venv\Scripts\activate en Windows
   ```

2. Instala dependencias:
   ```
   pip install -r requirements.txt
   ```

   **Nota:** se incluye la librería `sentencepiece`, necesaria para que el
   modelo de resumen funcione correctamente.

3. Crea un archivo `.streamlit/secrets.toml` con tu clave de API de OpenAI:
   ```toml
   OPENAI_API_KEY = "TU_CLAVE"
   ```

4. Ejecuta la app:
   ```
   streamlit run app.py
   ```

## Ejemplo en funcionamiento

![demo](https://placehold.co/600x300?text=Demo+resumidor)
