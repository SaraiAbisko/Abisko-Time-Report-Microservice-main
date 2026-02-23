from flask import request, jsonify
from DB.objects.estado import Estados

def create_estado_instance():
    data = request.get_json()

    if not data or "nombre" not in data:
        return jsonify({"error": "Missing 'nombre' field"}), 400

    estado = Estados(id=0, nombre=data["nombre"])
    inserted_id = estado.create_estados()

    return jsonify({
        "message": "Estado creado exitosamente",
        "id": inserted_id,
        "estado": estado.nombre
    }), 201