# 📚 PagePal: Tu Asistente de Lectura Personal

PagePal es una aplicación web y API RESTful construida con Python y FastAPI que permite a los usuarios guardar artículos de internet para leerlos más tarde. La aplicación extrae automáticamente el contenido principal del artículo, eliminando anuncios y otros elementos superfluos, para ofrecer una experiencia de lectura limpia y sin distracciones.

## ✨ Características Principales

-   **Guardado Sencillo:** Guarda cualquier artículo de la web simplemente pegando su URL.
-   **Extracción de Contenido Inteligente:** Utiliza `newspaper3k` para analizar y extraer el título y el cuerpo del texto de forma automática.
-   **Lectura sin Distracciones:** Accede a una lista de tus artículos guardados y léelos en una interfaz limpia.
-   **API RESTful:** Expone endpoints para crear y leer artículos, permitiendo la integración con otras aplicaciones.
-   **Base de Datos Persistente:** Almacena todos los artículos guardados utilizando SQLite y SQLAlchemy.
-   **Interfaz Web Dinámica:** Frontend interactivo construido con plantillas Jinja2, servido directamente desde FastAPI.

## 🛠️ Stack Tecnológico

-   **Backend:** Python 3, FastAPI
-   **Servidor ASGI:** Uvicorn
-   **Base de Datos:** SQLite
-   **ORM:** SQLAlchemy
-   **Validación de Datos:** Pydantic
-   **Extracción de Contenido Web:** Newspaper3k
-   **Frontend:** HTML5, Jinja2

## 🚀 Cómo Empezar

Sigue estos pasos para ejecutar el proyecto en tu máquina local.

### Prerrequisitos

-   Python 3.8+
-   Git

### Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/TiagoV69/PagePal-personal-reading-assistant.git
    cd PagePal-personal-reading-assistant
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    # En macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # En Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instala las dependencias del proyecto:**
    ```bash
    pip install -r requirements.txt
    ```

### Ejecución

1.  **Inicia el servidor de desarrollo:**
    ```bash
    uvicorn pagepal.main:app --reload
    ```

2.  **¡Abre la aplicación!**
    Abre tu navegador web y ve a `http://127.0.0.1:8000`.

3.  **Explora la API (Opcional):**
    Puedes interactuar con la API directamente a través de la documentación autogenerada en `http://127.0.0.1:8000/docs`.