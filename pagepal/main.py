
from fastapi import FastAPI

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

