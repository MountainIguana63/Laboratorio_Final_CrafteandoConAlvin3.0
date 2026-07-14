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
    libro = obtener_libro_por_id(libro_id)

    if libro is None:
        return jsonify({"error": "Libro no encontrado"}), 404

    return jsonify(libro), 200

@app.post("/libros")
def crear_libro():
    libro = request.get_json(silent=True)

    if not isinstance(libro, dict):
        return jsonify({"error": "Debe enviar los datos del libro en formato JSON"}), 400

    campos_faltantes = sorted(CAMPOS_OBLIGATORIOS - libro.keys())
    if campos_faltantes:
        return jsonify({
            "error": "Faltan campos obligatorios",
            "campos_faltantes": campos_faltantes,
        }), 400

    resultado = insertar_libro(libro)
    return jsonify(resultado), 201

@app.put("/libros/<int:libro_id>")
def modificar_libro(libro_id):
    libro_existente = obtener_libro_por_id(libro_id)

    if libro_existente is None:
        return jsonify({"error": "Libro no encontrado"}), 404

    cambios = request.get_json(silent=True)

    if not isinstance(cambios, dict) or not cambios:
        return jsonify({"error": "Debe enviar los cambios en formato JSON"}), 400

    # El id llega en la URL; no debe modificarse desde el cuerpo de la petición.
    cambios.pop("id", None)

    if not cambios:
        return jsonify({"error": "No se enviaron campos para actualizar"}), 400

    resultado = actualizar_libro(libro_id, cambios)
    return jsonify(resultado), 200

@app.delete("/libros/<int:id>")
def eliminar(id):
    resultado = eliminar_libro(id)
    return jsonify(resultado), 200

@app.errorhandler(Exception)
def manejar_error(error):
    # Durante el laboratorio permite observar errores sin ocultarlos completamente.
    return jsonify({"error": str(error)}), 500

if __name__ == "__main__":
    app.run(debug=True)
