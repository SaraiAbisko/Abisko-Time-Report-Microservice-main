from flask import request, jsonify
from DB.objects.consultor_modelo import ConsultorModelo

def get_consultor_modelo_instance():
    id_consultor = request.args.get("id_consultor", type=int)

    if "id_consultor" in request.args and id_consultor is None:
        return jsonify({"error": "'id_consultor' must be an integer"}), 400

    if id_consultor:
        consultores = ConsultorModelo.get_consultores(id_consultor)
    else:
        consultores = ConsultorModelo.get_all_consultores()
        
        
    response = [
        {
            "id_consultor": c.id_consultor,
            "nombre": c.nombre,
            "apellido": c.apellido,
            "correo_electronico": c.correo_electronico,
            "telefono": c.telefono
        }
        for c in consultores
    ]
    
    return jsonify(response), 200
