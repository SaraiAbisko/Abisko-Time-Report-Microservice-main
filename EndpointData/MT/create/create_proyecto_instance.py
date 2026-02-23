from flask import request, jsonify
from DB.objects.proyecto import Proyecto
from DB.crud import BaseRepository

def create_proyecto_instance():
    data = request.get_json()

    required = ["nombre", "fecha_inicio", "fecha_fin", "costo", "descripcion",
                "cliente_id", "servicio_id", "proyecto_estado", "imputable"]
    missing = [field for field in required if field not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    # Validar FK cliente
    if not BaseRepository.read("cliente", {"id": data["cliente_id"]}):
        return jsonify({"error": f"Cliente con ID {data['cliente_id']} no existe"}), 404

    # Validar FK servicio
    if not BaseRepository.read("servicio", {"id": data["servicio_id"]}):
        return jsonify({"error": f"Servicio con ID {data['servicio_id']} no existe"}), 404

    # Validar FK estado
    if not BaseRepository.read("estados", {"id": data["proyecto_estado"]}):
        return jsonify({"error": f"Estado con ID {data['proyecto_estado']} no existe"}), 404

    proyecto = Proyecto(
        id=0,
        nombre=data["nombre"],
        fecha_inicio=data["fecha_inicio"],
        fecha_fin=data["fecha_fin"],
        costo=data["costo"],
        descripcion=data["descripcion"],
        cliente_id=data["cliente_id"],
        servicio_id=data["servicio_id"],
        proyecto_estado=data["proyecto_estado"],
        imputable=data["imputable"]
    )

    inserted_id = proyecto.create_proyecto()

    return jsonify({
        "message": "Proyecto creado exitosamente",
        "id": inserted_id
    }), 201
