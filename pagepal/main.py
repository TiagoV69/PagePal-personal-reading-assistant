
from fastapi import FastAPI
from . import schemas  # Importamos nuestros esquemas
from datetime import datetime
from . import schemas, models # Importamos models
from .database import engine # Importamos el engine

# Esta línea le dice a SQLAlchemy que cree todas las tablas definidas
# en nuestros modelos (en este caso, solo la tabla 'articles').
# Se ejecutará una sola vez cuando la aplicación se inicie.
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PagePal API",
    description="Una API para guardar y leer artículos más tarde.",
    version="0.1.0",
)

@app.get("/")
def read_root():
    """
    Este sera el endpoint raiz de la aplicacion que se esta creando
    Devolvera un mensaje de bienvenidaa :D
    """
    return {"message": "¡Bienvenido a PagePal! Tu asistente de lectura personal."}

# Nuevo endpoint para "crear" un artículo.
# FastAPI se encarga de:
# 1. Leer el cuerpo (body) de la petición HTTP.
# 2. Validar que los datos coinciden con el modelo `schemas.ArticleCreate`.
# 3. Si no son válidos, devuelve un error 422 automáticamente.
# 4. Si son válidos, nos pasa los datos como un objeto Python.
@app.post("/articles/", response_model=schemas.Article)
def create_article(article: schemas.ArticleCreate):
    """
    Recibe la URL de un artículo, la "procesa" y la devuelve.
    (Por ahora, solo simulamos el procesamiento).
    """
    # Simulación: Por ahora no extraemos nada, solo devolvemos datos de ejemplo.
    # El `id` y `created_at` los generaría la base de datos.
    # El `title` y `content` los generaría nuestro scraper.
    mock_article_data = {
        "id": 1,
        "url": article.url,
        "title": "Título de Ejemplo Extraído",
        "content": "Este sería el contenido del artículo, limpio y legible...",
        "created_at": datetime.utcnow()
    }
    return mock_article_data
