from sqlalchemy.orm import Session
from . import models, schemas, services

def get_article(db: Session, article_id: int):
    """
    Busca un artículo en la base de datos por su ID.
    """
    return db.query(models.Article).filter(models.Article.id == article_id).first()

def create_article(db: Session, article: schemas.ArticleCreate):
    """
    Crea un nuevo artículo en la base de datos, extrayendo primero
    el contenido real de la URL.
    """
     # Llamamos a nuestro nuevo servicio para obtener el contenido
    extracted_data = services.extract_article_content(url=str(article.url))

    # Usamos los datos extraídos para crear el objeto de la BD
    db_article = models.Article(
        url=str(article.url),
        title=extracted_data["title"],
        content=extracted_data["content"]
    )
    
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article