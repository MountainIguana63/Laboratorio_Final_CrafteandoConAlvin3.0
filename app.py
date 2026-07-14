"""API REST del catálogo de libros."""
from flask import Flask, jsonify, request
from database import (
    obtener_libros, obtener_libro_por_id, insertar_libro,
    actualizar_libro, eliminar_libro
)

app = Flask(__name__)

@app.get("/")
def inicio():
    return jsonify({"mensaje": "API de libros en funcionamiento"}), 200

@app.get("/libros")
def listar_libros():
    return jsonify(obtener_libros()), 200

@app.get("/libros/<int:libro_id>")
def consultar_libro(libro_id):
    # TODO: llamar a obtener_libro_por_id y responder 404 cuando no exista.
    return jsonify({"mensaje": "Endpoint pendiente"}), 501

@app.post("/libros")
def crear_libro():
    # TODO: leer request.get_json(), validar campos obligatorios e insertar.
    return jsonify({"mensaje": "Endpoint pendiente"}), 501

@app.put("/libros/<int:libro_id>")
def modificar_libro(libro_id):
    # TODO: comprobar existencia, leer cambios y actualizar.
    return jsonify({"mensaje": "Endpoint pendiente"}), 501

@app.delete("/libros/<int:libro_id>")
def borrar_libro(libro_id):
    # TODO: comprobar existencia, eliminar y responder correctamente.
    return jsonify({"mensaje": "Endpoint pendiente"}), 501

@app.errorhandler(Exception)
def manejar_error(error):
    # Durante el laboratorio permite observar errores sin ocultarlos completamente.
    return jsonify({"error": str(error)}), 500

if __name__ == "__main__":
    app.run(debug=True)
