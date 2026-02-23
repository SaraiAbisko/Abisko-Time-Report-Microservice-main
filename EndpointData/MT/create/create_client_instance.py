from flask import request, jsonify
from DB.objects.cliente import Client

def create_client_instance():
    data = request.get_json()

    if not data or "nombre" not in data:
        return jsonify({"error": "Missing 'nombre' field"}), 400

    client = Client(id=0, nombre=data["nombre"])
    inserted_id = client.create_client()

    return jsonify({
        "message": "Client created successfully",
        "id": inserted_id,
        "nombre": client.nombre
    }), 201
