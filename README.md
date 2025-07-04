# Resumidor de PDFs con IA

Una aplicación en Python + Streamlit que resume automáticamente documentos PDF usando la API de OpenAI.

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
