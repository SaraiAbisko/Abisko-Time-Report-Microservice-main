from flask import request, jsonify
from DB.objects.consultor import Consultor
from DB.crud import BaseRepository

def create_consultor_instance():
    data = request.get_json()

    required_fields = ["nombre", "coste_hora", "numero_telefono"]
    missing = [f for f in required_fields if f not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    consultor = Consultor(
        id=0,
        nombre=data["nombre"],
        coste_hora=data["coste_hora"],
        numero_telefono=data["numero_telefono"]
    )

    inserted_id = consultor.create()

    return jsonify({
        "message": "Consultor registrado exitosamente",
        "id": inserted_id
    }), 201
