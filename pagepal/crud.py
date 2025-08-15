from sqlalchemy.orm import Session
from . import models, schemas

def get_article(db: Session, article_id: int):
    """
    Busca un artículo en la base de datos por su ID.
    """
    return db.query(models.Article).filter(models.Article.id == article_id).first()

def create_article(db: Session, article: schemas.ArticleCreate):
    """
    Crea un nuevo artículo en la base de datos.
    Por ahora, el título y el contenido son valores placeholder.
    """
    # Creamos un objeto del modelo de SQLAlchemy con los datos del esquema Pydantic.
    # NOTA: Aún no estamos extrayendo el contenido real. ¡Eso viene después!
    db_article = models.Article(
        url=str(article.url), # Convertimos la HttpUrl de Pydantic a string
        title="(Título pendiente de extracción)",
        content="(Contenido pendiente de extracción)"
    )
    db.add(db_article)  # Añade el objeto a la sesión de la BD.
    db.commit()         # Confirma los cambios en la BD (guarda).
    db.refresh(db_article) # Refresca el objeto con los datos de la BD (como el id).
    return db_article