"""
Acceso a datos.

Responsabilidad: toda interacción con Supabase debe permanecer en este archivo.
No colocar llamadas a Supabase directamente en app.py.
"""
from supabase import create_client, Client
from config import SUPABASE_URL, SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def obtener_libros():
    """Devuelve todos los libros ordenados por id."""
    respuesta = supabase.table("libros").select("*").order("id").execute()
    return respuesta.data

def obtener_libro_por_id(libro_id: int):
    """TODO 1: consultar un libro por su id y devolverlo o None."""
    # Pista: utilice .eq("id", libro_id) y revise respuesta.data.
    raise NotImplementedError("Endpoint pendiente: GET /libros/<id>")

def insertar_libro(datos: dict):
    """TODO 2: insertar un libro y devolver el registro creado."""
    # Pista: table(...).insert(datos).execute()
    raise NotImplementedError("Endpoint pendiente: POST /libros")

def actualizar_libro(libro_id: int, cambios: dict):
    """TODO 3: actualizar sólo el libro indicado y devolverlo."""
    # IMPORTANTE: update() siempre debe combinarse con un filtro.
    raise NotImplementedError("Endpoint pendiente: PUT /libros/<id>")

def eliminar_libro(libro_id: int):
    """TODO 4: eliminar sólo el libro indicado y devolver el eliminado."""
    # IMPORTANTE: delete() siempre debe combinarse con un filtro.
    raise NotImplementedError("Endpoint pendiente: DELETE /libros/<id>")
