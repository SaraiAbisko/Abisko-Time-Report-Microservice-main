from flask import request, jsonify
from DB.objects.servicio import Servicio
from DB.crud import BaseRepository

def create_servicio_instance():
    data = request.get_json()

    required_fields = ["nombre_servicio", "descripcion_servicio", "tipo_cobro_id"]
    missing = [field for field in required_fields if field not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    # Validar que tipo_cobro exista
    tipo_cobro = BaseRepository.read("tipo_cobro", {"id": data["tipo_cobro_id"]})
    if not tipo_cobro:
        return jsonify({"error": f"Tipo de cobro con ID {data['tipo_cobro_id']} no existe"}), 404

    servicio = Servicio(
        id=0,
        nombre_servicio=data["nombre_servicio"],
        descripcion_servicio=data["descripcion_servicio"],
        tipo_cobro_id=data["tipo_cobro_id"]
    )
    inserted_id = servicio.create()

    return jsonify({
        "message": "Servicio creado exitosamente",
        "id": inserted_id
    }), 201
