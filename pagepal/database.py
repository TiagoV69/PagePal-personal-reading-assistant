from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Definimos la URL de conexión a la base de datos.
# "sqlite:///./pagepal.db" significa que usaremos SQLite y el archivo
# de la base de datos se llamará 'pagepal.db' y estará en el directorio raíz.
SQLALCHEMY_DATABASE_URL = "sqlite:///./pagepal.db"

# 2. Creamos el "motor" de SQLAlchemy.
# El argumento connect_args es específico para SQLite, asegura que
# la misma conexión sea utilizada en diferentes hilos (threads).
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Creamos una clase SessionLocal, que será la fábrica de sesiones de base de datos.
# Cada instancia de SessionLocal será una sesión de base de datos.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Creamos una clase Base. Nuestros modelos de tabla ORM heredarán de esta clase.
Base = declarative_base()