from flask import request, jsonify
from DB.objects.servicio_modelo import ServicioModelo

def get_servicio_modelo_instance():
    id_servicio = request.args.get("id_servicio", type=int)

    if "id_servicio" in request.args and id_servicio is None:
        return jsonify({"error": "'id_servicio' must be an integer"}), 400

    if id_servicio:
        servicios = ServicioModelo.get_servicios(id_servicio)
    else:
        servicios = ServicioModelo.get_all_servicios()
        
        
    response = [
        {
            "id_servicio": c.id_servicio,
            "nombre_servicio": c.nombre_servicio,
            "descripcion_servicio": c.descripcion_servicio,
            "tipo_cobro": c.tipo_cobro,
            "horas_relacionadas": c.horas_relacionadas
        }
        for c in servicios
    ]
    
    return jsonify(response), 200