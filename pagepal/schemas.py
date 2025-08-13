from pydantic import BaseModel, HttpUrl
from datetime import datetime

# Clase base que comparte los campos comunes
# Sirve para no repetir código en las otras clases (principio DRY).
class ArticleBase(BaseModel):
    url: HttpUrl  # Pydantic validará que esto sea una URL válida.

# Modelo para la creación de un artículo.
# El usuario solo necesita proporcionar la URL.
class ArticleCreate(ArticleBase):
    pass  # No necesita campos adicionales por ahora.

# Modelo completo del artículo, usado para las respuestas de la API.
# Incluye los campos que la base de datos y nuestro backend generarán.
class Article(ArticleBase):
    id: int
    title: str
    content: str  # El contenido extraído del artículo
    created_at: datetime

    # Configuración para que Pydantic funcione con modelos de SQLAlchemy
    # que veremos más adelante. Nos permite mapear directamente desde la BD.
    class Config:
        orm_mode = True