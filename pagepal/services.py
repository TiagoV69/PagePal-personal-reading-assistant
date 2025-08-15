from newspaper import Article, ArticleException
import traceback # Importamos esta librería para imprimir errores detallados

def extract_article_content(url: str) -> dict:
    """
    Usa la librería newspaper3k para extraer el título y el contenido
    principal de la URL de un artículo. Ahora con manejo de errores mejorado.
    """
    try:
        article = Article(url)
        
        # Descargamos el contenido HTML de la página.
        article.download()
        
        # Analizamos el HTML para encontrar el contenido principal.
        article.parse()
        
        # Una comprobación extra: si no hay texto, lo indicamos.
        if not article.text:
            return {
                "title": article.title or "Título encontrado, pero sin contenido de artículo.",
                "content": "La página fue procesada, pero no se pudo identificar un cuerpo de texto principal."
            }

        return {
            "title": article.title,
            "content": article.text
        }
    except ArticleException as e:
        # Esto es para errores específicos de Newspaper al procesar un artículo
        print(f"Error de Newspaper3k al procesar la URL: {e}")
        return {
            "title": "Error al procesar el artículo",
            "content": f"Newspaper3k no pudo procesar la URL. Es posible que no sea un artículo válido. Error: {e}"
        }
    except Exception as e:
        # ¡Este es nuestro nuevo bloque! Captura CUALQUIER otro error.
        # (Ej: problemas de red, SSL, timeouts, etc.)
        print("--- OCURRIÓ UN ERROR INESPERADO EN EL SERVICIO DE EXTRACCIÓN ---")
        traceback.print_exc() # Imprime el error completo y detallado en la consola.
        print("---------------------------------------------------------------")
        return {
            "title": "Error Inesperado en la Extracción",
            "content": f"Ocurrió un error general al intentar acceder o procesar la URL. Revisa la consola del servidor para más detalles. Error: {str(e)}"
        }