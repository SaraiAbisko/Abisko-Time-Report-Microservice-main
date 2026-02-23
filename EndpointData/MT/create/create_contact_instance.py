from flask import request, jsonify
from DB.crud import BaseRepository
from DB.objects.contacto import Contacto

def create_contact_instance():
    data = request.get_json()

    # Validación de estructura básica
    required_fields = ["nombre_contacto", "correo_electronico", "numero_telefono", "cliente_id"]
    missing = [field for field in required_fields if field not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {', '.join(missing)}"}), 400

    # Validar que el cliente exista
    cliente_result = BaseRepository.read("cliente", {"id": data["cliente_id"]})
    if not cliente_result:
        return jsonify({"error": f"Client with id {data['cliente_id']} does not exist"}), 404

    # Crear contacto
    contact = Contacto(
        id=0,
        nombre_contacto=data["nombre_contacto"],
        correo_electronico=data["correo_electronico"],
        numero_telefono=data["numero_telefono"],
        cliente_id=data["cliente_id"]
    )
    inserted_id = contact.create_contact()

    return jsonify({
        "message": "Contacto creado exitosamente",
        "id": inserted_id
    }), 201