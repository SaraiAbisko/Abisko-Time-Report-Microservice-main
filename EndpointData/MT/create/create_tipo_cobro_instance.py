from flask import request, jsonify
from DB.objects.tipo_cobro import TipoCobro

def create_tipo_cobro_instance():
    data = request.get_json()

    required_fields = ["tipo_cobro", "horas_relacionadas"]
    missing = [field for field in required_fields if field not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    tipo = TipoCobro(
        id=0,
        tipo_cobro=data["tipo_cobro"],
        horas_relacionadas=data["horas_relacionadas"]
    )
    inserted_id = tipo.create()

    return jsonify({
        "message": "Tipo de cobro creado exitosamente",
        "id": inserted_id
    }), 201
