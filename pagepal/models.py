from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base # Importamos la Base que creamos

# Este es nuestro modelo de tabla. SQLAlchemy lo usará para crear la tabla 'articles'.
class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, index=True)
    title = Column(String)
    content = Column(String)
    # Usamos func.now() para que la base de datos ponga la fecha y hora automáticamente
    # al crear un registro.
    created_at = Column(DateTime(timezone=True), server_default=func.now())