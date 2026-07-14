"""Cliente sencillo para comprobar la API desde Python."""
import requests

BASE_URL = "http://127.0.0.1:5000"

def mostrar_respuesta(respuesta):
    print(f"Estado: {respuesta.status_code}")
    if respuesta.content:
        try:
            print(respuesta.json())
        except ValueError:
            print(respuesta.text)
    print("-" * 50)

if __name__ == "__main__":
    print("1. Consultar catálogo")
    mostrar_respuesta(requests.get(f"{BASE_URL}/libros", timeout=10))

    # Descomente progresivamente cuando cada endpoint esté implementado.
    # nuevo = {"titulo": "Clean Code", "autor": "Robert C. Martin", "anio": 2008, "disponible": True}
    # mostrar_respuesta(requests.post(f"{BASE_URL}/libros", json=nuevo, timeout=10))

    # cambios = {"disponible": False}
    # mostrar_respuesta(requests.put(f"{BASE_URL}/libros/1", json=cambios, timeout=10))

    # mostrar_respuesta(requests.delete(f"{BASE_URL}/libros/1", timeout=10))
