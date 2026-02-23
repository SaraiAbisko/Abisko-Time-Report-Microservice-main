from flask import request, jsonify
from DB.crud import BaseRepository

def create_trabajo_realizado_instance():
    data = request.get_json()

    # Campos que realmente existen en 'trabajo_realizado'
    required_fields = [
        "nombre_actividad",
        "horas_invertidas",
        "hora_extra",
        "asignacion_id",
        "fecha",
    ]
    missing = [f for f in required_fields if f not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    # Validar FK: asignacion_proyecto existe (y opcionalmente que esté activa)
    asignacion = BaseRepository.read("asignacion_proyecto", {"id": data["asignacion_id"]})
    if not asignacion:
        return jsonify({"error": f"Asignación con ID {data['asignacion_id']} no existe"}), 404
    # Si quieres exigir que esté activa:
    # if not asignacion[0].get("activo", True):
    #     return jsonify({"error": "La asignación existe pero no está activa"}), 409

    payload = {
        "nombre_actividad": data["nombre_actividad"],
        "horas_invertidas": data["horas_invertidas"],
        "hora_extra": data["hora_extra"],
        "asignacion_id": data["asignacion_id"],
        "fecha": data["fecha"],   # ← agregado
    }

    inserted_id = BaseRepository.create("trabajo_realizado", payload)

    return jsonify({
        "message": "Trabajo registrado exitosamente",
        "id": inserted_id
    }), 201