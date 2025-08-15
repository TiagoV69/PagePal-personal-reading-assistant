
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, models, crud
from .database import engine, SessionLocal
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

# --- Dependencia de la Base de Datos ---
def get_db():
    """
    Esta función es una dependencia. Por cada petición,
    creará una nueva sesión de BD, la entregará y se asegurará de cerrarla.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- AQUI REALIZAMOS LOS ENDPOINTS --- #

# Endpoint para traer todos los articulos
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
def create_article_endpoint(
    article: schemas.ArticleCreate, db: Session = Depends(get_db)
):
    """
    Recibe la URL de un artículo, lo guarda en la base de datos
    y devuelve el artículo creado.
    """
    # Ya no simulamos, ¡llamamos a nuestra función CRUD para guardar en la BD!
    return crud.create_article(db=db, article=article)

# Endopoint para leer un articulo por ID
@app.get("/articles/{article_id}", response_model=schemas.Article)
def read_article_endpoint(article_id: int, db: Session = Depends(get_db)):
    """
    Busca y devuelve un artículo por su ID.
    """
    db_article = crud.get_article(db, article_id=article_id)
    if db_article is None:
        # Si el artículo no existe, devolvemos un error 404 Not Found.
        raise HTTPException(status_code=404, detail="Artículo no encontrado")
    return db_article
