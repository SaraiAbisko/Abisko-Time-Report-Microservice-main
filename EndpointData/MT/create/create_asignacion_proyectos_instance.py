from flask import request, jsonify
from DB.objects.asignacion_proyectos import Asignacion_proyecto
from DB.crud import BaseRepository

def create_asignacion_proyecto_instance():
    data = request.get_json()

    required_fields = ["proyecto_id", "consultor_id", "activo"]
    missing = [field for field in required_fields if field not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    # Validar que proyecto exista
    proyecto = BaseRepository.read("proyecto", {"id": data["proyecto_id"]})
    if not proyecto:
        return jsonify({"error": f"Proyecto con ID {data['proyecto_id']} no existe"}), 404

    # Validar que consultor exista
    consultor = BaseRepository.read("consultor", {"id": data["consultor_id"]})
    if not consultor:
        return jsonify({"error": f"Consultor con ID {data['consultor_id']} no existe"}), 404

    asignacion = Asignacion_proyecto(
        id=0,
        proyecto_id=data["proyecto_id"],
        consultor_id=data["consultor_id"],
        activo=data["activo"]
    )
    inserted_id = asignacion.create()

    return jsonify({
        "message": "Asignación creada exitosamente",
        "id": inserted_id
    }), 201
